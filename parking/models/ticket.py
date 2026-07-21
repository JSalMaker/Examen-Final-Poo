##from datetime import datetime
class Ticket:
    def __init__(self, vehicle: Vehicle, slot_id: int, entry_time: datetime):
        self.vehicle = vehicle
        self.slot_id = slot_id
        self.entry_time = entry_time 
    def calculate_free(self, hours: float) -> float:
        if isinstance(self.vehicle, Car):
            valor_ticket = 5000 * hours
        else:
            valor_ticket = 3000 * hours
        if self.vehicle.is_member:
            valor_ticket = valor_ticket * 0.10
        return valor_ticket
