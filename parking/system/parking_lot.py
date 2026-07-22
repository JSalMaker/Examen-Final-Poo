from queue import Queue
from models.car import Car
from models.motorcycle import Motorcycle
from system.parking_slot import ParkingSlot
from exceptions.parking_full_error import ParkingFullError
from exceptions.vehicle_not_found_error import VehicleNotFoundError

class ParkingLot:
    def __init__(self, name: str, slots: list[ParkingSlot]):
        self.name = name
        self._slots= slots
        self._waiting_queue: Queue[Car | Motorcycle] = Queue()

    def park_vehicle(self, vehicle: Car | Motorcycle):
        try:
            for slot in self._slots:
                if not slot._is_occupied():
                    slot.park(vehicle)
                    return vehicle.ticket
               
            self._waiting_queue.put(vehicle)
            raise ParkingFullError(f"No hay cupos disponibles, se encuentra en lista de espera. Parqueaderos ocupados: {len(self._slots)}")
        except ParkingFullError as e:
            print (f"{e}\n")
            


    def exit_vehicle(self, plate: str):
        for slot in self._slots:

            if slot._is_occupied():
                vehicle = slot.get_vehicle()

                if vehicle and vehicle.license_plate == plate.upper():
                    fee = vehicle.ticket.calculate_fee()
                    slot.vacate()
                    print (f"La tarifa a pagar es de {fee}")

                    if not self._waiting_queue.empty():
                        next_v = self._waiting_queue.get()
                        slot.park(next_v)
                        print(f"El vehículo con placa {next_v.license_plate} ha sido parqueado en el puesto {slot._id}")

                    return
        try:
            raise VehicleNotFoundError(f"El vehiculo con placa {plate} no fue encontrado.")
        except VehicleNotFoundError as e:
            print(f"{e}\n")
                    
    def available_count(self):
        counter = 0
        available_slots = []

        for slot in self._slots:
            if not slot._is_occupied():
                available_slots.append(slot._id)
                counter +=1

        print(f"Parqueaderos disponibles: {counter}")
        if counter != 0:
            print("Los ID de éstos son:")

        for i, available_slot in enumerate(available_slots, start = 1):
            print(i, available_slot)

        return counter

    def occupied_vehicles(self):
        for slot in self._slots:
            if slot._is_occupied():
                yield slot._id, slot.get_vehicle()
    