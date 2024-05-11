class Sucursal:
    def __init__(self, id_sucursal, nombre, ubicacion, direccion, telefono, persona_cargo):
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.direccion = direccion
        self.telefono = telefono
        self.persona_cargo = persona_cargo

    def __str__(self):
        return f"Sucursal: {self.nombre} - Ubicación: {self.ubicacion}"
