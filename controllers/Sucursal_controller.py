from models.Sucursal import Sucursal
from models.SQLmanager import SQLManager

class SucursalController:
    def __init__(self, sql_manager):
        self.sql_manager = sql_manager

    def create_sucursal(self, nombre, ubicacion, direccion, telefono, persona_cargo):
        new_sucursal = Sucursal(None, nombre, ubicacion, direccion, telefono, persona_cargo)
        sucursal_id = self.sql_manager.create_sucursal(nombre, ubicacion, direccion, telefono, persona_cargo)
        new_sucursal.id_sucursal = sucursal_id
        return new_sucursal

    def get_all_sucursales(self):
        sucursales_data = self.sql_manager.get_all_sucursales()
        sucursales = [Sucursal(*sucursal_data) for sucursal_data in sucursales_data]
        return sucursales

    def update_sucursal(self, id_sucursal, nombre, ubicacion, direccion, telefono, persona_cargo):
        self.sql_manager.update_sucursal(id_sucursal, nombre, ubicacion, direccion, telefono, persona_cargo)

    def delete_sucursal(self, id_sucursal):
        self.sql_manager.delete_sucursal(id_sucursal)
