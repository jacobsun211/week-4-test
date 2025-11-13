import json
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()
items = []


def Load_data():
    with open('store_data/data.json', 'r') as f:
        data1 = json.load(f)
    return data1


def Save_data(data):
    with open('store_data/data.json', 'w') as f:
        json.dump(data, f)


@app.get('/items/')
def get_items():
    items = Load_data()
    return items


@app.put('/items/{item_id}')
def create_item(
        item_id: int,
        price: int):
    new_item = {'item_id': item_id, 'price': price}
    items = Load_data()
    for item in items:
        if item['item_id'] == new_item['item_id']:
            item['price'] = new_item['price']
            Save_data(items)
            return f'price of {new_item} updated'
    items.append(new_item)
    Save_data(items)
    return f'{new_item} created'


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)


