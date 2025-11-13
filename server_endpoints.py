import json
from json import JSONDecodeError

from fastapi import FastAPI
import uvicorn
from data.encrypt_decrypt import caesar,fence_encrypt,fence_decrypt

app = FastAPI()
items = []

#BONUS
def json_update(url,method):
    try:
        with open('store_data/endpoints_data.json','r')as f:
            data = json.load(f)
        for endpoint in data:
            if endpoint['url'] == url and endpoint['method'] == method:
                endpoint['stats']['total_requests_received'] += 1
                with open('store_data/endpoints_data.json','w')as f:
                    json.dump(data,f)
                return
    except:
        data.append(
            {"url":url,
             "method":method,
             "stats":{
            "total_requests_received":1,
           "avg_handling_time":None}
             }
        )
    with open('store_data/endpoints_data.json', 'w') as f:
        json.dump(data, f)
#BONUS


@app.get('/test')
def get_msg():
    json_update('/test','get')
    return  { 'msg': 'hi from test'}


@app.get('/name/{name}')
def get_name(name:str):
    with open('endpoints/name.txt', 'a+')as f:
        f.write(f'\n{name}')
    json_update('/name', 'get')
    return {'added':name}


@app.post('/caesar')
def caesar_cipher(
    text: str,
    offset:int,
    mode:str):
    json_update('/caesar', 'post')
    if mode == 'encrypt':
        return {'encrypted text':caesar(text,offset)}
    elif mode == 'decrypt':
        offset -= offset * 2
        return {'decrypted text':caesar(text,offset)}
    return 'invalid mode'


@app.get('/fence/encrypt')
def encrypt(text:str):
    encrypted = fence_encrypt(text)
    json_update('/fence/encrypt', 'get')
    return {'encrypted':encrypted}



@app.post('/fence/encrypt')
def decrypt(text:str):
    decrypted = fence_decrypt(text)
    json_update('/fence/encrypt', 'post')
    return {'decrypted':decrypted}

print(get_msg())



