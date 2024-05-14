from models.Cliente import Cliente
from datetime import datetime  # Importamos datetime para obtener la fecha actual
from models.MovimientoInventario import MovimientoInventario  # Importamos el modelo de MovimientoInventario

class ClienteController:
    def __init__(self, sql_manager, movimiento_controller):
        self.sql_manager = sql_manager
        self.movimiento_controller = movimiento_controller  # Agregamos el controlador de movimientos

    def create_cliente(self, nombre, direccion, telefono):
        # Crear un nuevo objeto Cliente
        new_cliente = Cliente(None, nombre, direccion, telefono)

        # Guardar el cliente en la base de datos
        cliente_id = self.sql_manager.create_cliente(nombre, direccion, telefono)
        new_cliente.id_cliente = cliente_id

        # Registrar el movimiento de creación de cliente
        movimiento = MovimientoInventario(None, "Creación de cliente", datetime.now(), 1, 0, None, None, cliente_id)
        self.movimiento_controller.create_movimiento(movimiento)

        # Devolver el cliente guardado
        return new_cliente

    def update_cliente(self, id_cliente, nombre, direccion, telefono):
        # Actualizar el cliente en la base de datos
        self.sql_manager.update_cliente(id_cliente, nombre, direccion, telefono)

        # Registrar el movimiento de actualización de cliente
        movimiento = MovimientoInventario(None, "Actualización de cliente", datetime.now(), 1, 0, None, None, id_cliente)
        self.movimiento_controller.create_movimiento(movimiento)

    def delete_cliente(self, id_cliente):
        # Registrar el movimiento de eliminación de cliente antes de eliminarlo de la base de datos
        movimiento = MovimientoInventario(None, "Eliminación de cliente", datetime.now(), 1, 0, None, None, id_cliente)
        self.movimiento_controller.create_movimiento(movimiento)

        # Eliminar el cliente de la base de datos
        self.sql_manager.delete_cliente(id_cliente)
