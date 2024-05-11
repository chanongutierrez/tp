from tkinter import Tk, Button
from models.SQLmanager import SQLManager
from views.Producto_view import ProductoView
from views.Cliente_view import ClienteView
from views.Proveedor_view import ProveedorView
from views.Deposito_view import DepositoView
from views.Sucursal_view import SucursalView
from views.MovimientoInventario_view import MovimientoInventarioView

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestión")
        # Configuramos los datos de conexión a la base de datos
        db_host = "localhost"
        db_name = "app_inventario"
        db_user = "chanon"
        db_password = "Niko1402"

        # Creamos una instancia de SQLManager con los datos de conexión
        self.sql_manager = SQLManager(db_host, db_name, db_user, db_password)
        self.sql_manager.connection  # Abrir la conexión al iniciar la aplicación

        # Configuramos los botones para cada vista
        self.producto_button = Button(master, text="Productos", command=self.open_producto_view)
        self.producto_button.pack()

        self.cliente_button = Button(master, text="Clientes", command=self.open_cliente_view)
        self.cliente_button.pack()

        self.proveedor_button = Button(master, text="Proveedores", command=self.open_proveedor_view)
        self.proveedor_button.pack()

        self.deposito_button = Button(master, text="Depósitos", command=self.open_deposito_view)
        self.deposito_button.pack()

        self.sucursal_button = Button(master, text="Sucursales", command=self.open_sucursal_view)
        self.sucursal_button.pack()

        self.movimiento_button = Button(master, text="Movimientos de Inventario", command=self.open_movimiento_view)
        self.movimiento_button.pack()

    def open_producto_view(self):
        producto_view = ProductoView(self.sql_manager)
        producto_view.iniciar()

    def open_cliente_view(self):
        cliente_view = ClienteView(self.sql_manager)
        cliente_view.iniciar()

    def open_proveedor_view(self):
        proveedor_view = ProveedorView(self.sql_manager)
        proveedor_view.iniciar()

    def open_deposito_view(self):
        deposito_view = DepositoView(self.sql_manager)
        deposito_view.iniciar()

    def open_sucursal_view(self):
        sucursal_view = SucursalView(self.sql_manager)
        sucursal_view.iniciar()

    def open_movimiento_view(self):
        movimiento_view = MovimientoInventarioView(self.sql_manager)
        movimiento_view.iniciar()

    def close(self):
        self.sql_manager.close_connection()  # Cerrar la conexión al salir de la aplicación
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MainApplication(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
