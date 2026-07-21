from models.car import Car
from models.motorcycle import Motorcycle
from system.parking_lot import ParkingLot
from system.parking_slot import ParkingSlot
def main():
    s1 =  ParkingSlot("s1")
    s2 = ParkingSlot("s2")
    s3 = ParkingSlot("s3")
    s4 = ParkingSlot("s4")
    slots = [s1,s2, s3, s4]
    mall_centro = ParkingLot("Mall Centro", slots)

    while True:
        print("--------------------------------------")
        print("------ BIENVENIDO A MALL CENTER ------")
        print("--------------------------------------")
        print("Escriba el número la acción a realizar:")
        print("1. Parquear carro")
        print("2. Parquear moto")
        print("3. Sacar vehículo")
        print("4. Salir del menu")

        opc = input("\nOpción:")
        
        if opc == "1":
            l_p = str(input("\nPlaca del vehículo: "))
            o_n = str(input("Nombre del propietario: "))
            d_n = int(input("¿Cuántas puertas tiene: ?"))
            m = int (input("¿Es miembro? Escriba 1 para si, 0 para no: "))
            while m != 0 and m != 1:
                m = int(input("Recuerde, debe ser 1 o 0: "))

            member_bool = (m == 1)
            car = Car(l_p, o_n, member_bool, d_n)
            mall_centro.park_vehicle(car)


        elif opc == "2":
            l_p = str(input("\nPlaca de la moto: "))
            o_n = str(input("Nombre del propietario: "))
            s_c = int(input("¿Tiene sidecar? Escriba 1 para si, 0 para no: "))
            while s_c != 0 and s_c != 1:
                s_c = int(input("Recuerde, debe ser 1 o 0: "))

            m = int (input("¿Es miembro? Escriba 1 para si, 0 para no: "))
            while m != 0 and m != 1:
                m = int(input("Recuerde, debe ser 1 o 0: "))

            sidecar_bool = (s_c == 1)
            member_bool = (m == 1)
            motorcycle = Motorcycle(l_p, o_n, member_bool, sidecar_bool)

            mall_centro.park_vehicle(motorcycle)

        elif opc == "3":
            l_p = str(input("\nEscriba la placa del vehículo:"))
            mall_centro.exit_vehicle(l_p)
        
        elif opc == "4":
            print ("\nGracias por usar nuestros servicios. Tenga buen día.")
            break
        
        else:
            print("Recuerde que debe ser alguna opción del menú.")