from exceptions.slot_occupied_error import SlotOccupiedError
import uuid
from models.ticket import Ticket
class ParkingSlot:
    def __init__(self, id: str):
        self._id = str(uuid.uuid1())[:5] 
        self._vehicle = None 
        
         
    def __str__(self):
        return ( 
        f"Parqueadero numero :{self._id}\n"
        f"Parqueadero Ocupado: {self._is_occupied()}\n"
        f"Vehiculo Obtenido: {self.get_vehicle()}\n"
        )

    def park(self, vehicle) -> bool:
        if self._is_occupied():
            raise SlotOccupiedError("Puesto ocupado, intente con otro lugar", vehicle)
    
        else:
            
            
                self.set_vehicle(vehicle)
                vehicle.ticket = Ticket(vehicle, self._id)
                print(f"El vehiculo de placas {vehicle.license_plate} está parqueando en el espacio {self._id}")
                print(f"{vehicle.get_name()}, Gracias por ocupar nuestro espacio")
                return True
            
    def vacate(self):
        print(f"{self._vehicle.get_name},  Muchas Gracias por su visita\n")
        self._vehicle = None


    def set_vehicle(self,vehicle):
        self._vehicle = vehicle
    
    def get_vehicle(self):
        print(self._vehicle)
    
    def _is_occupied(self):
        if self._vehicle:
            return True
        else: 
            return False








