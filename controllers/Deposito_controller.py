from models.Deposito import Deposito
from datetime import datetime  # Importamos datetime para obtener la fecha actual
from models.MovimientoInventario import MovimientoInventario  # Importamos el modelo de MovimientoInventario

class DepositoController:
    def __init__(self, sql_manager, movimiento_controller):
        self.sql_manager = sql_manager
        self.movimiento_controller = movimiento_controller  # Agregamos el controlador de movimientos

    def create_deposito(self, nombre, ubicacion, direccion, telefono, persona_cargo):
        new_deposito = Deposito(None, nombre, ubicacion, direccion, telefono, persona_cargo)
        deposito_id = self.sql_manager.create_deposito(nombre, ubicacion, direccion, telefono, persona_cargo)
        new_deposito.id_deposito = deposito_id

        # Registramos el movimiento de creación de depósito
        movimiento = self.movimiento_controller.create_movimiento(tipo="Creación de depósito", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=deposito_id, id_proveedor=None)

        return new_deposito

    def update_deposito(self, id_deposito, nombre, ubicacion, direccion, telefono, persona_cargo):
        # Antes de actualizar el depósito, registramos el movimiento de actualización
        old_deposito = self.sql_manager.get_deposito_by_id(id_deposito)
        movimiento = self.movimiento_controller.create_movimiento(tipo="Actualización de depósito", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=id_deposito, id_proveedor=None)

        self.sql_manager.update_deposito(id_deposito, nombre, ubicacion, direccion, telefono, persona_cargo)

    def delete_deposito(self, id_deposito):
        # Antes de eliminar el depósito, registramos el movimiento de eliminación
        movimiento = self.movimiento_controller.create_movimiento(tipo="Eliminación de depósito", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=id_deposito, id_proveedor=None)

        self.sql_manager.delete_deposito(id_deposito)
