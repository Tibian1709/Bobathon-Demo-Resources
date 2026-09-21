"""
Inventory Allocation Engine
Ingram Micro Distribution Operations

This module contains core inventory logic for allocating items across multiple regional
distribution centres (Millington TN, Mira Loma CA, Carol Stream IL), managing backorders,
and handling priority allocation for Platinum Partners.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

class AllocationStatus(str, Enum):
    FULLY_ALLOCATED = "FULLY_ALLOCATED"
    PARTIALLY_ALLOCATED = "PARTIALLY_ALLOCATED"
    BACKORDERED = "BACKORDERED"
    REJECTED = "REJECTED"

@dataclass
class WarehouseStock:
    warehouse_id: str
    location_name: str
    available_qty: int
    reserved_qty: int = 0

@dataclass
class AllocationResult:
    sku: str
    requested_qty: int
    allocated_qty: int
    backordered_qty: int
    status: AllocationStatus
    warehouse_breakdown: Dict[str, int] = field(default_factory=dict)

class InventoryAllocator:
    def __init__(self, initial_inventory: Optional[Dict[str, List[WarehouseStock]]] = None):
        # Key: SKU, Value: List of WarehouseStock sorted by fulfilment priority
        self.inventory: Dict[str, List[WarehouseStock]] = initial_inventory or {}

    def allocate(self, sku: str, requested_qty: int, is_priority_partner: bool = False) -> AllocationResult:
        if requested_qty <= 0:
            return AllocationResult(
                sku=sku,
                requested_qty=requested_qty,
                allocated_qty=0,
                backordered_qty=0,
                status=AllocationStatus.REJECTED
            )

        if sku not in self.inventory:
            return AllocationResult(
                sku=sku,
                requested_qty=requested_qty,
                allocated_qty=0,
                backordered_qty=requested_qty,
                status=AllocationStatus.BACKORDERED
            )

        warehouses = self.inventory[sku]
        allocated = 0
        breakdown: Dict[str, int] = {}
        remaining_needed = requested_qty

        for wh in warehouses:
            # Priority partners are permitted to draw up to 50% into reserved buffer
            usable_stock = wh.available_qty
            if is_priority_partner and wh.reserved_qty > 0:
                usable_buffer = wh.reserved_qty // 2
                usable_stock += usable_buffer

            if usable_stock > 0:
                fulfill_from_wh = min(usable_stock, remaining_needed)
                wh.available_qty -= fulfill_from_wh
                if wh.available_qty < 0:
                    # Drew into reserved buffer
                    borrowed = abs(wh.available_qty)
                    wh.reserved_qty -= borrowed
                    wh.available_qty = 0

                breakdown[wh.warehouse_id] = fulfill_from_wh
                allocated += fulfill_from_wh
                remaining_needed -= fulfill_from_wh

            if remaining_needed == 0:
                break

        backordered = requested_qty - allocated
        if allocated == requested_qty:
            status = AllocationStatus.FULLY_ALLOCATED
        elif allocated > 0:
            status = AllocationStatus.PARTIALLY_ALLOCATED
        else:
            status = AllocationStatus.BACKORDERED

        return AllocationResult(
            sku=sku,
            requested_qty=requested_qty,
            allocated_qty=allocated,
            backordered_qty=backordered,
            status=status,
            warehouse_breakdown=breakdown
        )
