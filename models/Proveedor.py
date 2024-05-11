class Proveedor:
    def __init__(self, id_proveedor, nombre, direccion, telefono, forma_pago, plazo_entrega):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.forma_pago = forma_pago
        self.plazo_entrega = plazo_entrega

    def __str__(self):
        return f"Proveedor: {self.nombre} - Teléfono: {self.telefono}"
