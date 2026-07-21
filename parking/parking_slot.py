from .models.vehicle import Vehicle
from .exceptions.slot_occupied_error import SlotOccupiedError
from uuid import uuid

class ParkingSlot:
    def __init__(self, vehicle: Vehicle):
        self._id = str(uuid.uuid1()[:5]) 
        self._vehicle = vehicle 
        
         
    def __str__(self):
        return ( 
        f"Parqueadero numero :{self.id}\n"
        f"Vehiculo Obtenido: {self.get_vehicle}\n"
        f"Parqueadero Ocupado: {self.is_occupied()}"
        )

    def park(self, vehicle) -> bool:
        if self._is_occupied():
            raise SlotOccupiedError("Puesto ocupado, intente con otro lugar", vehicle)
    
        else:
            
                self.vacate()
                self.set_vehicle(vehicle)
                print(f"El vehiculo de placas {self._vehicle.license_plate} está parqueando en el espacio {self._id}")
                print(f"{self._vehicle.get_name()}, Gracias por ocupar nuestro espacio")
                return True
            
    def vacate(self):
        print(f"{self._vehicle.get_name} Muchas Gracias por su visita")
        self._vehicle = None


    def set_vehicle(self,vehicle):
        self._vehicle = vehicle
    
    def get_vehicle(self):
        print(self.vehicle)
    
    def _is_occupied(self):
        if self.vehicle:
            return True
        else: 
            return False








