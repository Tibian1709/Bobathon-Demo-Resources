"""
Monolithic Order Fulfilment Pipeline (Ingram Micro Simulated Legacy System)
Tightly coupled synchronous architecture demonstrating bottlenecks before microservice decomposition.
"""

import time
import json
from typing import Dict, Any

class MonolithicOrderFulfilmentSystem:
    def __init__(self):
        self.orders_db = {}
        self.inventory_db = {
            "M365-BP": 500,
            "CISCO-DUO": 300,
            "CISCO-ROUTER-9K": 12
        }
        self.audit_log = []

    def fulfill_order_synchronous_blocking(self, order_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Antipattern: A single blocking transaction executing 6 downstream systems synchronously.
        If any step hangs (e.g. ERP or email gateway), the entire checkout blocks and times out.
        """
        order_id = f"IM-ORD-{int(time.time()*1000)}"
        partner_id = order_payload.get("partner_id")
        items = order_payload.get("items", [])
        
        print(f"[*] Step 1: Ingesting order {order_id} for partner {partner_id}")
        
        # Step 2: Synchronous Inventory Check & Lock
        print("[*] Step 2: Locking database rows and deducting stock synchronously...")
        for item in items:
            sku = item["sku"]
            qty = item["qty"]
            if self.inventory_db.get(sku, 0) < qty:
                return {"status": "FAILED", "error": f"Insufficient stock for {sku}"}
            self.inventory_db[sku] -= qty
            
        # Step 3: Synchronous ERP Ledger Write
        print("[*] Step 3: Calling Mainframe / Legacy SAP ERP connector over synchronous SOAP...")
        # Simulating latency
        time.sleep(0.1)
        
        # Step 4: Synchronous Vendor Cloud License Provisioning API
        print("[*] Step 4: Provisioning SaaS license with Microsoft / Cisco upstream vendor...")
        time.sleep(0.1)
        
        # Step 5: Synchronous Shipping / Warehouse Dispatch
        print("[*] Step 5: Sending picking instruction to Millington DC warehouse queue...")
        
        # Step 6: Synchronous Notification Email Dispatch
        print("[*] Step 6: Triggering partner confirmation email via SMTP gateway...")
        
        self.orders_db[order_id] = {
            "order_id": order_id,
            "partner_id": partner_id,
            "items": items,
            "status": "COMPLETED",
            "timestamp": time.time()
        }
        
        print(f"[✓] Order {order_id} completed successfully in blocking pipeline.")
        return {"status": "SUCCESS", "order_id": order_id}

if __name__ == "__main__":
    monolith = MonolithicOrderFulfilmentSystem()
    order = {
        "partner_id": "APEX-CLOUD-01",
        "items": [
            {"sku": "M365-BP", "qty": 25},
            {"sku": "CISCO-DUO", "qty": 25}
        ]
    }
    res = monolith.fulfill_order_synchronous_blocking(order)
    print("Execution Result:", res)
