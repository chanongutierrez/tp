from models.Sucursal import Sucursal
from datetime import datetime  # Importamos datetime para obtener la fecha actual

class SucursalController:
    def __init__(self, sql_manager, movimiento_controller):  # Agregamos el controlador de movimientos como parámetro
        self.sql_manager = sql_manager
        self.movimiento_controller = movimiento_controller

    def create_sucursal(self, nombre, ubicacion, direccion, telefono, persona_cargo):
        new_sucursal = Sucursal(None, nombre, ubicacion, direccion, telefono, persona_cargo)
        sucursal_id = self.sql_manager.create_sucursal(nombre, ubicacion, direccion, telefono, persona_cargo)
        new_sucursal.id_sucursal = sucursal_id

        # Registramos el movimiento de creación de sucursal
        movimiento = self.movimiento_controller.create_movimiento(tipo="Creación de sucursal", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=sucursal_id, id_proveedor=None)

        return new_sucursal

    def update_sucursal(self, id_sucursal, nombre, ubicacion, direccion, telefono, persona_cargo):
        # Antes de actualizar la sucursal, registramos el movimiento de actualización
        old_sucursal = self.sql_manager.get_sucursal_by_id(id_sucursal)
        movimiento = self.movimiento_controller.create_movimiento(tipo="Actualización de sucursal", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=id_sucursal, id_proveedor=None)

        self.sql_manager.update_sucursal(id_sucursal, nombre, ubicacion, direccion, telefono, persona_cargo)

    def delete_sucursal(self, id_sucursal):
        # Antes de eliminar la sucursal, registramos el movimiento de eliminación
        movimiento = self.movimiento_controller.create_movimiento(tipo="Eliminación de sucursal", fecha=datetime.now(), cantidad=1, precio_unitario=0, id_producto=None, id_deposito_sucursal=id_sucursal, id_proveedor=None)

        self.sql_manager.delete_sucursal(id_sucursal)
