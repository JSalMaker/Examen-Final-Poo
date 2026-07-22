from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.car import Car
    from models.motorcycle import Motorcycle

class Ticket:
    def __init__(self, vehicle: Car | Motorcycle , slot_id: str):
        self.vehicle = vehicle
        self.slot_id = slot_id
        self.entry_time = datetime.now()

    def calculate_fee(self) -> str:
        from models.car import Car

        time = datetime.now() - self.entry_time
        seconds = time.total_seconds()
        hours = seconds/3600

        valor_ticket: float = 0
        if isinstance(self.vehicle, Car):
            valor_ticket = 5000 * hours
            if self.vehicle._is_member:
                valor_ticket = valor_ticket * 0.90
        
        else:
            valor_ticket = 3000 * hours
            if self.vehicle._is_member:
                valor_ticket = valor_ticket * 0.90
        
        return (f"Cobro total: {valor_ticket}")
