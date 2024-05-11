from tkinter import Tk, Button
from utils.DatabaseManager import DatabaseManager
from utils.UIManager import UIManager
class MainApplication:
    def __init__(self, master):
        self.master = master
        self.db_manager = DatabaseManager("localhost", "app_inventario", "chanon", "Niko1402")
        self.ui_manager = UIManager(master, ["Productos", "Clientes", "Proveedores", "Depósitos", "Sucursales", "Movimientos de Inventario"], self.db_manager)
        self.db_manager.connect()
        self.ui_manager.setup_ui()
       

    def setup_buttons(self):
        # Configuramos los botones para cada vista
        for view_name in self.ui_manager.view_names:
            button = Button(self.master, text=view_name, command=lambda vn=view_name: self.open_view(vn))
            button.pack()

    def open_view(self, view_name):
        view = self.ui_manager.create_view(view_name)
        view.iniciar()

    def close(self):
        self.db_manager.close_connection()
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MainApplication(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
