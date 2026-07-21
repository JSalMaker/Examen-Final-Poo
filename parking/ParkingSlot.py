from .models.vehicle import Vehicle
from .exceptions import SlotOccupiedError
from uuid import uuid

class ParkingSlot:
    def __init__(self, vehicle: Vehicle):
        self.id = str(uuid.uuid4()[:5])
        self._vehicle = vehicle if vehicle else None
        
         
    def __str__(self):
        f"Parqueadero numero :{self.id}\n"
        f"Vehiculo Obtenido: {self.get_vehicle}\n"
        f"Parqueadero Ocupado: {self.is_occupied(self)}"
        

    def park(self, vehicle) -> bool:
        if self._is_occupied:
            raise NotImplementedError("Puesto ocupado, intente con otro lugar")
    
        else:
            
                self.unpark()
                self.set_vehicle(vehicle)
                print(f"El vehiculo de placas {self.vehicle.license_plate} está parqueando en el espacio {self.id}")
                print(f"{self.vehicle.get_name}, Gracias por ocupar nuestro espacio")
                return True
            
    def unpark(self):
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








