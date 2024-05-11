import mysql.connector

class SQLManager:
    def __init__(self, db_host, db_name, db_user, db_password):
        self.connection = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )

    def create_producto(self, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo):
        sql = """
            INSERT INTO productos (nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo))
        self.connection.commit()
        id_producto = cursor.lastrowid
        cursor.close()
        return id_producto

    def get_all_productos(self):
        sql = """
            SELECT * FROM productos;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)
        productos = cursor.fetchall()
        cursor.close()
        return productos

    def update_producto(self, id_producto, nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo):
        sql = """
            UPDATE productos
            SET nombre = %s, descripcion = %s, precio_compra = %s, precio_venta = %s, categoria = %s, marca = %s, fecha_vencimiento = %s, stock_minimo = %s, unidad_medida = %s, tipo = %s
            WHERE id_producto = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo, id_producto))
        self.connection.commit()
        cursor.close()

    def delete_producto(self, id_producto):
        sql = """
            DELETE FROM productos
            WHERE id_producto = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_producto,))
        self.connection.commit()
        cursor.close()


    def create_sucursal(self, nombre, ubicacion, direccion, telefono, persona_cargo):
        sql = """
            INSERT INTO sucursales (nombre, ubicacion, direccion, telefono, persona_cargo)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, ubicacion, direccion, telefono, persona_cargo))
        self.connection.commit()
        sucursal_id = cursor.lastrowid
        cursor.close()
        return sucursal_id

    def get_all_sucursales(self):
        sql = """
            SELECT * FROM sucursales;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)
        sucursales = cursor.fetchall()
        cursor.close()
        return sucursales

    def update_sucursal(self, id_sucursal, nombre, ubicacion, direccion, telefono, persona_cargo):
        sql = """
            UPDATE sucursales
            SET nombre = %s, ubicacion = %s, direccion = %s, telefono = %s, persona_cargo = %s
            WHERE sucursal_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, ubicacion, direccion, telefono, persona_cargo, id_sucursal))
        self.connection.commit()
        cursor.close()

    def delete_sucursal(self, id_sucursal):
        sql = """
            DELETE FROM sucursales
            WHERE sucursal_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_sucursal,))
        self.connection.commit()
        cursor.close()

    def create_cliente(self, nombre, direccion, telefono):
        sql = """
            INSERT INTO clientes (nombre, direccion, telefono)
            VALUES (%s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, direccion, telefono))
        self.connection.commit()
        cliente_id = cursor.lastrowid
        cursor.close()
        return cliente_id

    def get_all_clientes(self):
        sql = """
            SELECT * FROM clientes;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)
        clientes = cursor.fetchall()
        cursor.close()
        return clientes

    def update_cliente(self, id_cliente, nombre, direccion, telefono):
        sql = """
            UPDATE clientes
            SET nombre = %s, direccion = %s, telefono = %s
            WHERE cliente_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, direccion, telefono, id_cliente))
        self.connection.commit()
        cursor.close()

    def delete_cliente(self, id_cliente):
        sql = """
            DELETE FROM clientes
            WHERE cliente_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_cliente,))
        self.connection.commit()
        cursor.close()

    def create_deposito(self, nombre, ubicacion, direccion, telefono, persona_cargo):
        sql = """
            INSERT INTO depositos (nombre, ubicacion, direccion, telefono, persona_cargo)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, ubicacion, direccion, telefono, persona_cargo))
        self.connection.commit()
        deposito_id = cursor.lastrowid
        cursor.close()
        return deposito_id

    def get_all_depositos(self):
        sql = """
            SELECT * FROM depositos;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)
        depositos = cursor.fetchall()
        cursor.close()
        return depositos

    def update_deposito(self, id_deposito, nombre, ubicacion, direccion, telefono, persona_cargo):
        sql = """
            UPDATE depositos
            SET nombre = %s, ubicacion = %s, direccion = %s, telefono = %s, persona_cargo = %s
            WHERE deposito_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, ubicacion, direccion, telefono, persona_cargo, id_deposito))
        self.connection.commit()
        cursor.close()

    def delete_deposito(self, id_deposito):
        sql = """
            DELETE FROM depositos
            WHERE deposito_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_deposito,))
        self.connection.commit()
        cursor.close()

    def create_movimiento(self, tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor):
        sql = """
            INSERT INTO movimientos_inventario (tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor))
        self.connection.commit()
        movimiento_id = cursor.lastrowid
        cursor.close()
        return movimiento_id

    def get_all_movimientos(self):
        sql = """
            SELECT * FROM movimientos_inventario;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)
        movimientos = cursor.fetchall()
        cursor.close()
        return movimientos

    def update_movimiento(self, id_movimiento, tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor):
        sql = """
            UPDATE movimientos_inventario
            SET tipo = %s, fecha = %s, cantidad = %s, precio_unitario = %s, id_producto = %s, id_deposito_sucursal = %s, id_proveedor = %s
            WHERE movimiento_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (tipo, fecha, cantidad, precio_unitario, id_producto, id_deposito_sucursal, id_proveedor, id_movimiento))
        self.connection.commit()
        cursor.close()

    def delete_movimiento(self, id_movimiento):
        sql = """
            DELETE FROM movimientos_inventario
            WHERE movimiento_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_movimiento,))
        self.connection.commit()
        cursor.close()

    def create_proveedor(self, nombre, direccion, telefono, forma_pago, plazo_entrega):
        sql = """
            INSERT INTO proveedores (nombre, direccion, telefono, forma_pago, plazo_entrega)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, direccion, telefono, forma_pago, plazo_entrega))
        self.connection.commit()
        proveedor_id = cursor.lastrowid
        cursor.close()
        return proveedor_id

    def get_all_proveedores(self):
        sql = """
            SELECT * FROM proveedores;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql)
        proveedores = cursor.fetchall()
        cursor.close()
        return proveedores

    def update_proveedor(self, id_proveedor, nombre, direccion, telefono, forma_pago, plazo_entrega):
        sql = """
            UPDATE proveedores
            SET nombre = %s, direccion = %s, telefono = %s, forma_pago = %s, plazo_entrega = %s
            WHERE proveedor_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, direccion, telefono, forma_pago, plazo_entrega, id_proveedor))
        self.connection.commit()
        cursor.close()

    def delete_proveedor(self, id_proveedor):
        sql = """
            DELETE FROM proveedores
            WHERE proveedor_id = %s;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_proveedor,))
        self.connection.commit()
        cursor.close()

    def close_connection(self):
        self.connection.close()
