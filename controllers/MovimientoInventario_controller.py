from models.MovimientoInventario import MovimientoInventario
class MovimientoInventarioController:
    def __init__(self, sql_manager):
        self.sql_manager = sql_manager

    def create_movimiento(self, tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor):
        new_movimiento = MovimientoInventario(None, tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor)
        movimiento_id = self.sql_manager.create_movimiento(tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor)
        new_movimiento.id_movimiento = movimiento_id
        return new_movimiento

    def get_all_movimientos(self):
        movimientos_data = self.sql_manager.get_all_movimientos()
        movimientos = [MovimientoInventario(*movimiento_data) for movimiento_data in movimientos_data]
        return movimientos

    def update_movimiento(self, id_movimiento, tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor):
        self.sql_manager.update_movimiento(id_movimiento, tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor)

    def delete_movimiento(self, id_movimiento):
        self.sql_manager.delete_movimiento(id_movimiento)