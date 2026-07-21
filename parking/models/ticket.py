from models.vehicle import Vehicle

class Ticket:
    def __init__(self, vehicle: Vehicle, slot_id: str):
        self.vehicle = vehicle
        self.slot_id = slot_id

    def calculate_fee(self, hours: float) -> str:
        if self.vehicle.get_type()== 'Carro':
            valor_ticket = 5000 * hours
            if self.vehicle._is_member:
                 valor_ticket = valor_ticket * 0.10
                 return f"valor ticket: {str(valor_ticket)}"
    
        else:
            valor_ticket = 3000 * hours
            if self.vehicle._is_member:
                valor_ticket = valor_ticket * 0.1        
            return f"valor ticket: {str(valor_ticket)}"
        return f"valor ticket: {str(valor_ticket)}"
    