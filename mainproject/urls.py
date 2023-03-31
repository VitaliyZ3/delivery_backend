from fastapi import APIRouter
from .controllers import (
    create_delivery
)
router = APIRouter()

router.add_api_route('/deliveries/create', create_delivery, methods=['POST'])