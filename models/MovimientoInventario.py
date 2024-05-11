class MovimientoInventario:
    def __init__(self, id_movimiento, tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor):
        self.id_movimiento = id_movimiento
        self.tipo = tipo
        self.fecha = fecha
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.id_producto = id_producto
        self.id_deposito_sucursal = id_deposito_sucursal
        self.id_proveedor = id_proveedor

    def __str__(self):
        return f"""
                Movimiento Inventario:
                ID: {self.id_movimiento}
                Tipo: {self.tipo}
                Fecha: {self.fecha}
                Cantidad: {self.cantidad}
                Precio Unitario: {self.precio_unitario:.2f}
                Producto ID: {self.id_producto}
                Deposito/Sucursal ID: {self.id_deposito_sucursal}
                Proveedor ID (si aplica): {self.id_proveedor or 'N/A'}"""