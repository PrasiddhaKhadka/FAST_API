from fastapi import FastAPI

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

# Query Param
@app.get('/items/')
async def read_items(q: str,price:str = 100):
    return {"q": q,
            "price": price}


# default param
@app.get('/items/')
async def read_items(q: str = "foo"):
    return {"q": q}

# combining the both query param and default param
@app.get('/items/{item_id}/comment')
async def read_items(item_id: int, q: str = "foo"):
    return {"item_id": item_id,
            "q": q}
