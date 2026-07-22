from models.car import Car
from models.motorcycle import Motorcycle
from system.parking_lot import ParkingLot
from system.parking_slot import ParkingSlot

s1 =  ParkingSlot("s1")
s2 = ParkingSlot("s2")
slots = [s1,s2]
mall_centro = ParkingLot("Mall Centro", slots)

car1 = Car("ABC123", "Juan", True, 4)
motorcycle1 = Motorcycle("XYZ999", "Laura", False, False)
extra_car = Car ("LMN456", "Carlos", False, 2)

#Pruebas de parqueo
mall_centro.park_vehicle(car1)
mall_centro.park_vehicle(motorcycle1)

# print (slots[0])

mall_centro.park_vehicle(extra_car)

if car1.ticket is not None:
    print(car1.ticket.calculate_fee())

mall_centro.exit_vehicle("UCX451")
mall_centro.exit_vehicle("XYZ999")
mall_centro.available_count()

occupieds- mall_centro.occupied_vehicles()

for occupied in occupieds:
    print(occupied)


