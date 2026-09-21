"""
Legacy Order Processing Script
Ingram Micro Distribution Operations (Simulated Legacy Script)
NOTE: Contains intentional technical debt, lack of type annotations, hardcoded configs,
and unvalidated dictionary access for demonstration of Bob's refactoring capabilities.
"""

import sys
import json
import time

# Insecure/anti-pattern: global state and hardcoded configs
DEFAULT_TAX_RATE = 0.0825
CREDIT_LIMIT_OVERRIDE = 1000000.00
DEBUG_MODE = True

def process_order(raw_data):
    # Missing input validation / type checks
    print("DEBUG: Received raw order -> " + str(raw_data))
    
    order = raw_data
    partner_id = order['partner_id']
    items = order['items']
    
    total = 0.0
    processed_items = []
    
    for i in items:
        sku = i['sku']
        qty = i['qty']
        price = i['unit_price']
        
        # Insecure / no boundary check
        line_total = qty * price
        
        # Hardcoded promo rule without abstraction
        if sku.startswith("M365") and qty >= 50:
            print("Applying 5% bulk promo on " + sku)
            line_total = line_total * 0.95
            
        total += line_total
        processed_items.append({
            "sku": sku,
            "qty": qty,
            "unit_price": price,
            "final_line_price": line_total
        })
        
    tax = total * DEFAULT_TAX_RATE
    grand_total = total + tax
    
    # Primitive credit check simulation
    if grand_total > 50000.0:
        if order.get("partner_tier") != "Platinum":
            return {"status": "REJECTED", "reason": "Exceeds standard credit threshold"}
            
    res = {
        "order_id": "ORD-" + str(int(time.time())),
        "partner_id": partner_id,
        "items": processed_items,
        "subtotal": round(total, 2),
        "tax": round(tax, 2),
        "grand_total": round(grand_total, 2),
        "status": "APPROVED"
    }
    
    print("DEBUG: Output -> " + json.dumps(res))
    return res

if __name__ == "__main__":
    sample_order = {
        "partner_id": "PARTNER-8821",
        "partner_tier": "Gold",
        "items": [
            {"sku": "M365-BP", "qty": 100, "unit_price": 22.00},
            {"sku": "CISCO-DUO", "qty": 100, "unit_price": 6.00}
        ]
    }
    result = process_order(sample_order)
    print("Final Result:", result)
