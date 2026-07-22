import uuid
from models.ticket import Ticket
from exceptions.slot_occupied_error import SlotOccupiedError

class ParkingSlot:
    def __init__(self, id: str):
        self._id = id
        self._protected_ref = str(uuid.uuid1())[:5] 
        self._vehicle = None
        
         
    def __str__(self):
        return ( 
        f"Parqueadero numero :{self._id}\n"
        f"Parqueadero Ocupado: {self._is_occupied()}\n" # type: ignore
        f"{self.get_vehicle()}"
        )

    def park(self, vehicle) -> bool:
        if self._is_occupied():
            raise SlotOccupiedError("Puesto ocupado, intente con otro lugar", vehicle)
    
        else:
            self.set_vehicle(vehicle)
            vehicle.ticket = Ticket(vehicle, self._id)
            print(f"El vehiculo de placas {self._vehicle.license_plate} está parqueando en el espacio {self._id}\n") # type: ignore
            print(f"{self._vehicle.get_name()}, Gracias por ocupar nuestro espacio\n") # type: ignore
            return True
            
    def vacate(self):
        print(f"{self._vehicle.get_name()} , muchas gracias por su visita\n") # type: ignore
        self._vehicle = None


    def set_vehicle(self,vehicle):
        self._vehicle = vehicle
    
    def get_vehicle(self):
        return(self._vehicle)
    
    def _is_occupied(self):
        if self._vehicle:
            return True
        else: 
            return False