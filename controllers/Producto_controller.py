from models.Producto import Producto

class ProductoController:
    def __init__(self, sql_manager):
        self.sql_manager = sql_manager

    def create_producto(self, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo):
        # Crear un nuevo objeto Producto
        new_producto = Producto(None, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo)

        # Guardar el producto en la base de datos
        product_id = self.sql_manager.create_producto(nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo)
        new_producto.id_producto = product_id

        # Devolver el producto guardado
        return new_producto

    def get_all_productos(self):
        # Obtener todos los productos de la base de datos
        productos_data = self.sql_manager.get_all_productos()

        # Convertir registros de la base de datos en objetos Producto
        productos = [Producto(*producto_data) for producto_data in productos_data]

        # Devolver la lista de productos
        return productos

    def update_producto(self, id_producto, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo):
        # Actualizar el producto en la base de datos
        self.sql_manager.update_producto(id_producto, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo)

    def delete_producto(self, id_producto):
        # Eliminar el producto de la base de datos
        self.sql_manager.delete_producto(id_producto)
