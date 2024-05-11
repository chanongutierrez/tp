from models.Cliente import Cliente
from models.SQLmanager import SQLManager

class ClienteController:
    def __init__(self, sql_manager):
        self.sql_manager = sql_manager  # Corregido: Utiliza sql_manager directamente, sin instanciar nuevamente

    def create_cliente(self, nombre, direccion, telefono):
        # Create a new Cliente object
        new_cliente = Cliente(None, nombre, direccion, telefono)

        # Save the cliente in the database
        cliente_id = self.sql_manager.create_cliente(nombre, direccion, telefono)  # Corregido: Llama al método create_cliente del SQLManager
        new_cliente.id_cliente = cliente_id

        # Return the saved cliente
        return new_cliente

    def get_all_clientes(self):
        # Retrieve all clientes from the database
        clientes_data = self.sql_manager.get_all_clientes()  # Corregido: Llama al método get_all_clientes del SQLManager

        # Convert database records into Cliente objects
        clientes = [Cliente(*cliente_data) for cliente_data in clientes_data]

        # Return the list of clientes
        return clientes

    def update_cliente(self, id_cliente, nombre, direccion, telefono):
        # Update the cliente in the database
        self.sql_manager.update_cliente(id_cliente, nombre, direccion, telefono)  # Corregido: Llama al método update_cliente del SQLManager

    def delete_cliente(self, id_cliente):
        # Delete the cliente from the database
        self.sql_manager.delete_cliente(id_cliente)  # Corregido: Llama al método delete_cliente del SQLManager
