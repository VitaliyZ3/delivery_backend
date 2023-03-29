from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)

redis = get_redis_connection(
    host='redis-12997.c300.eu-central-1-1.ec2.cloud.redislabs.com',
    port='12997',
    password='kraS5CxDXC4618ZGUr0ru2yffdsjhSRr',
    decode_responses=True
)


class Delivery(HashModel):
    budget: int = 0
    notes: str = ''

    class Meta:
        database = redis

class Event(HashModel):
    delivery_id: str = None
    type: str
    data: str

    class Meta:
        database = redis

@app.post('/deliveries/create')
async def create_delivery(request: Request):
    body = await request.json()
    delivery = Delivery()
