from fastapi import FastAPI
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
