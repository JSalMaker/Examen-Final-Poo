from queue import Queue
from models.vehicle import Vehicle
from models.ticket import Ticket
from parking_slot import ParkingSlot
from exceptions.parking_full_error import ParkingFullError
from exceptions.vehicle_not_found_error import VehicleNotFoundError

class ParkingLot:
    def __init__(self, name: str, slots: list[ParkingSlot]):
        self.name = name
        self._slots= slots
        self._waiting_queue = Queue()

    def park_vehicle(self, vehicle: Vehicle):
        for slot in self._slots:
            if not slot.is_occupied():
                slot.park(vehicle)
                
                ticket = Ticket(vehicle, slot.slot_id, entry_time)
                
                return ticket
               
        self._waiting_queue.put(vehicle)
        raise ParkingFullError("No hay cupos disponibles, se encuentra en lista de espera.")


    def exit_vehicle(self, plate: str):
        for slot in self._slots:
            if slot.is_occupied():
                vehicle = slot.get_vehicle()

                if vehicle.license_plate == plate:
                    slot.vacate()

                    if not self._waiting_queue.empty():
                        next_v = self._waiting_queue.get()
                        slot.park(next_v)

                    return
                
        raise VehicleNotFoundError(f"El vehiculo con placa {plate} no fue encontrado.")
                    
    def available_count(self):
        counter = 0
        available_slots = []

        for slot in self._slots:
            if not slot.is_occupied():
                available_slots.append(slot.slot_id)
                counter +=1

        print(f"Parqueaderos disponibles: {counter}")
        print("Los ID de éstos son:")

        for i, available_slot in enumerate(available_slots, start = 1):
            print(i, available_slot)

        return counter

    def occupied_vehicles(self):
        for slot in self._slots:
            if slot.is_occupied():
                yield slot.slot_id, slot.get_vehicle()
    
