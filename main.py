from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection
from mainproject.urls import router as delivery_router

app = FastAPI()

app.include_router(delivery_router)

app.add_middleware(
    allow_methods=['*'],
    allow_headers=['*'],
)

redis = get_redis_connection(
    host='redis-12997.c300.eu-central-1-1.ec2.cloud.redislabs.com',
    port='12997',
    password='kraS5CxDXC4618ZGUr0ru2yffdsjhSRr',
    decode_responses=True
)

