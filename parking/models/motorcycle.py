from models.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str, owner_name: str, is_member:bool,  sidecar: bool):
        super().__init__(license_plate, owner_name, is_member)
        self.sidecar = sidecar

    def get_type(self):
        return ("Motocicleta")
    
    def __str__(self):
        return (
            f"Placa de la moto: {self.license_plate}\n"
            f"Nombre del propietario: {self.get_name()}\n"
            f"Tiene sidecar: {self.sidecar}\n"
        )
    
    
