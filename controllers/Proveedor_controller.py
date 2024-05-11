from models.Proveedor import Proveedor
from models.SQLmanager import SQLManager

class ProveedorController:
    def __init__(self, sql_manager):
        self.sql_manager = sql_manager

    def create_proveedor(self, nombre, direccion, telefono, forma_pago, plazo_entrega):
        new_proveedor = Proveedor(None, nombre, direccion, telefono, forma_pago, plazo_entrega)
        proveedor_id = self.sql_manager.create_proveedor(nombre, direccion, telefono, forma_pago, plazo_entrega)
        new_proveedor.id_proveedor = proveedor_id
        return new_proveedor

    def get_all_proveedores(self):
        proveedores_data = self.sql_manager.get_all_proveedores()
        proveedores = [Proveedor(*proveedor_data) for proveedor_data in proveedores_data]
        return proveedores

    def update_proveedor(self, id_proveedor, nombre, direccion, telefono, forma_pago, plazo_entrega):
        self.sql_manager.update_proveedor(id_proveedor, nombre, direccion, telefono, forma_pago, plazo_entrega)

    def delete_proveedor(self, id_proveedor):
        self.sql_manager.delete_proveedor(id_proveedor)
