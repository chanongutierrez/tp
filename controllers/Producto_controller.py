from models.Producto import Producto

from datetime import datetime  # Importamos datetime para obtener la fecha actual
from models.MovimientoInventario import MovimientoInventario  # Importamos el modelo de MovimientoInventario

class ProductoController:
    def __init__(self, sql_manager, movimiento_controller):
        self.sql_manager = sql_manager
        self.movimiento_controller = movimiento_controller  # Agregamos el controlador de movimientos

    def create_producto(self, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo):
        # Crear un nuevo objeto Producto
        new_producto = Producto(None, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo)

        # Guardar el producto en la base de datos
        product_id = self.sql_manager.create_producto(nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo)
        new_producto.id_producto = product_id

        # Registramos el movimiento de creación de producto
        movimiento = self.movimiento_controller.create_movimiento(tipo="Creación de producto", fecha=datetime.now(), cantidad=1, precio_unitario=precio_compra, id_producto=product_id, id_deposito_sucursal=None, id_proveedor=None)

        # Devolver el producto guardado
        return new_producto

    def update_producto(self, id_producto, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo):
        # Antes de actualizar el producto, registramos el movimiento de actualización
        old_producto = self.sql_manager.get_producto_by_id(id_producto)
        movimiento = self.movimiento_controller.create_movimiento(tipo="Actualización de producto", fecha=datetime.now(), cantidad=1, precio_unitario=precio_compra, id_producto=id_producto, id_deposito_sucursal=None, id_proveedor=None)

        self.sql_manager.update_producto(id_producto, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo)

    def delete_producto(self, id_producto):
        # Antes de eliminar el producto, registramos el movimiento de eliminación
        movimiento = self.movimiento_controller.create_movimiento(tipo="Eliminación de producto", fecha=datetime.now(), cantidad=1, precio_unitario=None, id_producto=id_producto, id_deposito_sucursal=None, id_proveedor=None)

        self.sql_manager.delete_producto(id_producto)
