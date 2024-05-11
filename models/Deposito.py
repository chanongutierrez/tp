class Deposito:
    def __init__(self, id_deposito, nombre, ubicacion, direccion, telefono, persona_cargo):
        self.id_deposito = id_deposito
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.direccion = direccion
        self.telefono = telefono
        self.persona_cargo = persona_cargo

    def __str__(self):
        return f"Depósito: {self.nombre} - Ubicación: {self.ubicacion}"
