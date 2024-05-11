from models.Deposito import Deposito
from models.SQLmanager import SQLManager

class DepositoController:
    def __init__(self, sql_manager):
        self.sql_manager = sql_manager

    def create_deposito(self, nombre, ubicacion, direccion, telefono, persona_cargo):
        new_deposito = Deposito(None, nombre, ubicacion, direccion, telefono, persona_cargo)
        deposito_id = self.sql_manager.create_deposito(nombre, ubicacion, direccion, telefono, persona_cargo)
        new_deposito.id_deposito = deposito_id
        return new_deposito

    def get_all_depositos(self):
        depositos_data = self.sql_manager.get_all_depositos()
        depositos = [Deposito(*deposito_data) for deposito_data in depositos_data]
        return depositos

    def update_deposito(self, id_deposito, nombre, ubicacion, direccion, telefono, persona_cargo):
        self.sql_manager.update_deposito(id_deposito, nombre, ubicacion, direccion, telefono, persona_cargo)

    def delete_deposito(self, id_deposito):
        self.sql_manager.delete_deposito(id_deposito)
