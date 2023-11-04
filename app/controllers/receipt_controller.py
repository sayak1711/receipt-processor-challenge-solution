# controllers/receipt_controller.py
import uuid
from fastapi import APIRouter, HTTPException, Depends
from app.models import Receipt
from app.services import process_receipt, calculate_points

def process_retailer(retailer_name):
    score = 0
    for c in retailer_name:
        if c.isalnum():
            score += 1
    return score

def process_total(total):
    score = 0
    if total%10 == 0:
        score += 50
    if total%0.25 == 0:
        score += 25
    return score

def process_items(items):
    score = len(items)//2
    for item in items:
        if len(item['shortDescription'].strip())%3 == 0:
            score += round(item['price']*0.2)

def process_date_time(purchase_date, purchase_time):
    score = 0
    day = int(purchase_date.split('-')[-1])
    if day%2 != 0:
        score += 6
    hour, minute = map(int(), purchase_time.split(':'))
    if (hour > 14 and hour < 16) or (hour == 14 and minute > 0):
        score += 10
    return score

points_dict = {}

router = APIRouter()

@router.post("/process", response_model=dict)
async def process_receipt_api(receipt: Receipt):
    score = 0
    score += process_retailer(receipt.get('retailer', ''))
    score += process_total(receipt.get('total', 0))
    score += process_items(receipt.get('items', []))
    score += process_date_time(receipt.get('purchaseDate', ''), receipt.get('purchaseTime', ''))
    receipt_id = str(uuid.uuid4())
    response = {"id": receipt_id}
    points_dict[receipt_id] = score
    return response

@router.get("/{id}/points", response_model=dict)
async def get_points_api(id: str):
    if id in points_dict:
        return {"points": points_dict[id]}
    else:
        raise HTTPException(status_code=404, detail="No receipt found for that id")
    
