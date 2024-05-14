from datetime import datetime  # Importamos datetime para obtener la fecha actual
from models.MovimientoInventario import MovimientoInventario  # Importamos el modelo de MovimientoInventario
from models import Proveedor
class ProveedorController:
    def __init__(self, sql_manager, movimiento_controller):
        self.sql_manager = sql_manager
        self.movimiento_controller = movimiento_controller  # Agregamos el controlador de movimientos

    def create_proveedor(self, nombre, direccion, telefono, forma_pago, plazo_entrega):
        new_proveedor = Proveedor(None, nombre, direccion, telefono, forma_pago, plazo_entrega)
        proveedor_id = self.sql_manager.create_proveedor(nombre, direccion, telefono, forma_pago, plazo_entrega)
        new_proveedor.id_proveedor = proveedor_id

        # Registramos el movimiento de creación de proveedor
        movimiento = self.movimiento_controller.create_movimiento(tipo="Creación de proveedor", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=None, id_proveedor=proveedor_id)

        return new_proveedor

    def update_proveedor(self, id_proveedor, nombre, direccion, telefono, forma_pago, plazo_entrega):
        # Antes de actualizar el proveedor, registramos el movimiento de actualización
        old_proveedor = self.sql_manager.get_proveedor_by_id(id_proveedor)
        movimiento = self.movimiento_controller.create_movimiento(tipo="Actualización de proveedor", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=None, id_proveedor=id_proveedor)

        self.sql_manager.update_proveedor(id_proveedor, nombre, direccion, telefono, forma_pago, plazo_entrega)

    def delete_proveedor(self, id_proveedor):
        # Antes de eliminar el proveedor, registramos el movimiento de eliminación
        movimiento = self.movimiento_controller.create_movimiento(tipo="Eliminación de proveedor", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=None, id_proveedor=id_proveedor)

        self.sql_manager.delete_proveedor(id_proveedor)
