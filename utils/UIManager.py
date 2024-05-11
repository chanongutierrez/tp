from tkinter import Tk, Button
from utils.ViewFactory import ViewFactory
class UIManager:
    def __init__(self, master, views, db_manager):
        self.master = master
        self.views = views
        self.db_manager = db_manager
        self.view_names = views  # No necesitas inicializar view_names si solo quieres usar las cadenas en views

    def setup_ui(self):
        self.master.title("Sistema de Gestión")
        for view_name in self.view_names:
            button = Button(self.master, text=view_name, command=lambda name=view_name: self.open_view(name))
            button.pack()

    def open_view(self, view_name):
        view = ViewFactory.create_view(view_name, self.master, self.db_manager.sql_manager)
        view.iniciar()
