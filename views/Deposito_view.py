from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, messagebox
from controllers.Deposito_controller import DepositoController
from controllers.MovimientoInventario_controller import MovimientoInventarioController
class DepositoView:
    def __init__(self, sql_manager):
        self.root = Tk()
        self.root.title("Gestión de Depósitos")
        movimiento_controller=MovimientoInventarioController(sql_manager)
        self.Deposito_controller = DepositoController(sql_manager,movimiento_controller)

        # Etiquetas y campos de entrada para agregar depósitos
        self.label_nombre = Label(self.root, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = Entry(self.root)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        self.label_ubicacion = Label(self.root, text="Ubicación:")
        self.label_ubicacion.grid(row=1, column=0, padx=10, pady=5)
        self.entry_ubicacion = Entry(self.root)
        self.entry_ubicacion.grid(row=1, column=1, padx=10, pady=5)

        self.label_direccion = Label(self.root, text="Dirección:")
        self.label_direccion.grid(row=2, column=0, padx=10, pady=5)
        self.entry_direccion = Entry(self.root)
        self.entry_direccion.grid(row=2, column=1, padx=10, pady=5)

        self.label_telefono = Label(self.root, text="Teléfono:")
        self.label_telefono.grid(row=3, column=0, padx=10, pady=5)
        self.entry_telefono = Entry(self.root)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=5)

        # Botones para operaciones CRUD
        self.btn_agregar = Button(self.root, text="Agregar", command=self.agregar_deposito)
        self.btn_agregar.grid(row=4, column=0, padx=10, pady=5)

        self.btn_listar = Button(self.root, text="Listar", command=self.listar_depositos)
        self.btn_listar.grid(row=4, column=1, padx=10, pady=5)

        # Texto y barra de desplazamiento para mostrar la lista de depósitos
        self.texto_depositos = Text(self.root, width=60, height=10)
        self.texto_depositos.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.scrollbar = Scrollbar(self.root, command=self.texto_depositos.yview)
        self.scrollbar.grid(row=5, column=2, sticky='nsew')
        self.texto_depositos.config(yscrollcommand=self.scrollbar.set)

    def agregar_deposito(self):
        nombre = self.entry_nombre.get()
        ubicacion = self.entry_ubicacion.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()

        if nombre and ubicacion and direccion and telefono:
            try:
                nuevo_deposito = self.deposito_controller.create_deposito(nombre, ubicacion, direccion, telefono)
                messagebox.showinfo("Éxito", f"Depósito {nuevo_deposito.nombre} agregado exitosamente con ID: {nuevo_deposito.id_deposito}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el depósito: {e}")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def listar_depositos(self):
        try:
            depositos = self.deposito_controller.get_all_depositos()
            if depositos:
                self.texto_depositos.delete(1.0, "end")
                for deposito in depositos:
                    self.texto_depositos.insert("end", f"ID: {deposito.id_deposito}, Nombre: {deposito.nombre}, Ubicación: {deposito.ubicacion}, Dirección: {deposito.direccion}, Teléfono: {deposito.telefono}\n")
            else:
                messagebox.showinfo("Información", "No hay depósitos registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar los depósitos: {e}")

    def iniciar(self):
        self.root.mainloop()


