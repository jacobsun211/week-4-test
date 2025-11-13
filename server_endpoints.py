import json
from fastapi import FastAPI
import uvicorn
from data.encrypt_decrypt import caesar,fence_encrypt,fence_decrypt

app = FastAPI()
items = []


@app.get('/test')
def get_msg():
    return  { 'msg': 'hi from test'}


@app.get('/name/{name}')
def get_name(name:str):
    with open('endpoints/name.txt', 'a+')as f:
        f.write(f'\n{name}')
    return {'added':name}


@app.post('/caesar')
def caesar_cipher(
    text: str,
    offset:int,
    mode:str):

    if mode == 'encrypt':
        return {'encrypted text':caesar(text,offset)}
    elif mode == 'decrypt':
        offset -= offset * 2
        return {'decrypted text':caesar(text,offset)}
    return 'invalid mode'


@app.get('/fence/encrypt')
def encrypt(text:str):
    encrypted = fence_encrypt(text)
    return {'encrypted':encrypted}



@app.post('/fence/encrypt')
def decrypt(text:str):
    decrypted = fence_decrypt(text)
    return {'decrypted':decrypted}


# uvicorn.run(app, host="localhost", port=8002)
