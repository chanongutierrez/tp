class Cliente:
    def __init__(self, id_cliente, nombre, direccion, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} - Teléfono: {self.telefono}"
