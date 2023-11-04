from app.models.models import Receipt
from fastapi import HTTPException
import math
import uuid

def process_retailer(retailer_name):
    score = 0
    for c in retailer_name:
        if c.isalnum():
            score += 1
    return score

def process_total(total):
    score = 0
    if total.endswith('.00'):
        score += 50
    if total.split('.')[1] in ['00', '25', '50', '75']:
        score += 25
    return score

def process_items(items):
    score = (len(items)//2)*5
    for item in items:
        if len(item.shortDescription.strip())%3 == 0:
            score += math.ceil(float(item.price)*0.2)
    return score

def process_date_time(purchase_date, purchase_time):
    score = 0
    day = int(purchase_date.split('-')[-1])
    if day%2 != 0:
        score += 6
    hour, minute = map(int, purchase_time.split(':'))
    if (hour > 14 and hour < 16) or (hour == 14 and minute > 0):
        score += 10
    return score

points_dict = {}

def process_receipt(receipt: Receipt) -> dict:
    score = 0
    score += process_retailer(receipt.retailer)
    score += process_total(receipt.total)
    score += process_items(receipt.items)
    score += process_date_time(receipt.purchaseDate, receipt.purchaseTime)
    receipt_id = str(uuid.uuid4())
    response = {"id": receipt_id}
    points_dict[receipt_id] = score
    return response

def calculate_points(id: str) -> int:
    if id in points_dict:
        return {"points": points_dict[id]}
    else:
        raise HTTPException(status_code=404, detail="No receipt found for that id")
