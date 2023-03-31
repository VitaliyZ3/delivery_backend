from redis_om import HashModel
from .main import redis

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