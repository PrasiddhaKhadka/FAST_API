from fastapi import FastAPI, Form
from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List
from uuid import UUID
from datetime import date, time, datetime, timedelta


class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: time
    end_date: date
    end_time: time
    execution_time: timedelta



class Profile(BaseModel):
    name: str
    age: int
    address: str

class Image(BaseModel):
    url: HttpUrl
    name: str


class Product(BaseModel):
    name: str = Field(title="Product 1")
    price: int = Field(title='Price of the item', description='The price must be greater than 0',gt=0)
    discount: int  = Field(title='0')
    discounted_price: int = Field(title='0')
    tags: Set[str] = Field(examples=['item1', 'item2'])
    image: List[Image] = []

    # FORM 
    

    # SAMPLE DATA 
    class Config:
        schema_extra = {
            'name': 'Product 1',
            'price': 100,
            'discount': 0,
            'discounted_price': 100,
            'tags':['item1', 'item2'],
            'image':[
                {
                    'url': 'https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png',
                    'name': 'FastAPI'
                }
            ]
        }

class Offer(BaseModel):
    name: str
    description: str
    price: float
    products: List[Product]


class UserModel(BaseModel):
    name: str
    age: int



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/product/{product_id}')
async def get_product(product_id: int):
    return {"product_id": product_id}


@app.get('/user/admin')
async def get_admin():
    return {"user": "admin"}

@app.get('/user/{user_name}')
async def get_user(user_name: str):
    return {"user_name": user_name}

# Query Param and Default Param
@app.get('/items/')
async def read_items(q: str,price:str = 100):
    return {"q": q,
            "price": price}



# combining the both query param and default param
@app.get('/items/{item_id}/comment')
async def read_items(item_id: int, q: str = "foo"):
    return {"item_id": item_id,
            "q": q}



@app.post('/profile')
async def create_profile(profile: Profile):
    return {
        "name": profile.name,
        "age": profile.age,
        "address": profile.address
    }



# PASSING THE PATH PARAMETER AND PYDANTIC MODEL
@app.post('/addproduct/{product_id}/category')
async def create_product(product: Product, product_id: int,category: str= 'Goods'):
    product.discounted_price = product.price - (product.price * product.discount / 100)
    return {
        "product_id": product_id,
        "category": category,
        "name": product.name,
        "price": product.price,
        "discount": product.discount,
        "discounted_price": product.discounted_price
    }



@app.post('/purchase')
async def create_user(product:Product, user: UserModel):
    return {
        "product": product,
        "user": user
    }


@app.get('/offer')
async def create_offer(offer: Offer):
    return {
        "offer": offer
    }

@app.post('/event')
async def create_event(event: Event):
    return {
        "event_id": event.event_id,
        "start_date": event.start_date,
        "start_time": event.start_time,
        "end_date": event.end_date,
        "end_time": event.end_time,
        "execution_time": event.execution_time
    }