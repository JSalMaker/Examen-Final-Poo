from models.vehicle import Vehicle
class SlotOccupiedError(Exception):
    def __init__(self,message, vehicle: Vehicle):
        super().__init__(message)
        print(f"vehiculo de placas {vehicle.get_name} estacionado en el slot")
    
