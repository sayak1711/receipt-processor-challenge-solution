from fastapi import APIRouter, HTTPException
from app.models.models import Receipt
from app.services.receipt_service import process_receipt, calculate_points

router = APIRouter()

@router.post("/receipts/process", response_model=dict)
async def process_receipt_api(receipt: Receipt):
    return process_receipt(receipt)

@router.get("/receipts/{id}/points", response_model=dict)
async def get_points_api(id: str):
    return calculate_points(id)
    
