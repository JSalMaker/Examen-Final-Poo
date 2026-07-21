from .car import Car
from .motorcycle import Motorcycle
from .system.parking_lot import ParkingLot
from .system.parking_slot import ParkingSlot
from exceptions.parking_full_error import ParkingFullError

def main():
    car1 = Car("ABC123","Juan",True,4)
    moto1 = Motorcycle("XYZ999","Laura",True,False)
    extra = Car("LMN456","Carlos", False,2)
    cupos = [ParkingSlot("S1"),ParkingSlot("S2")]
    parqueadero = ParkingLot("Mall Centro",cupos)

    parqueadero.park_vehicle(car1)
    print(cupos[0])
    parqueadero.park_vehicle(moto1)
    try:
        parqueadero.park_vehicle(extra)
    except ParkingFullError as msg:
        print(msg)

    print(extra.ticket.calculate_fee(3))
if __name__ == "__main__":
    main()