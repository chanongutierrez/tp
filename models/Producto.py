class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.categoria = categoria
        self.marca = marca
        self.fecha_vencimiento = fecha_vencimiento
        self.stock_minimo = stock_minimo
        self.unidad_medida = unidad_medida
        self.tipo = tipo

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio_venta}"
