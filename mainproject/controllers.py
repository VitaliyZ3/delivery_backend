from fastapi import Request
from .models import Delivery 

async def create_delivery(request: Request):
    body = await request.json()
    delivery = Delivery(budget=body['data']['budget'], notes=body['data']['budget']).save()
    return delivery