from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, license_plate: str, owner_name: str, door_number: int):
        super().__init__(license_plate, owner_name)
        self.door_number = door_number

    def get_type(self):
        return ("Carro")
    
    def __str__(self):
        return (
            f"Placa del carro: {self.license_plate}\n"
            f"Nombre del propietario; {self.get_name()}\n"
            f"Número de puertas: {self.door_number}\n"
        )
    
    
    