from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, messagebox
from controllers.Proveedor_controller import ProveedorController

class ProveedorView:
    def __init__(self, sql_manager):
        self.root = Tk()
        self.root.title("Gestión de Proveedores")
        self.proveedor_controller = ProveedorController(sql_manager)

        # Etiquetas y campos de entrada para agregar proveedores
        self.label_nombre = Label(self.root, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = Entry(self.root)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        self.label_direccion = Label(self.root, text="Dirección:")
        self.label_direccion.grid(row=1, column=0, padx=10, pady=5)
        self.entry_direccion = Entry(self.root)
        self.entry_direccion.grid(row=1, column=1, padx=10, pady=5)

        self.label_telefono = Label(self.root, text="Teléfono:")
        self.label_telefono.grid(row=2, column=0, padx=10, pady=5)
        self.entry_telefono = Entry(self.root)
        self.entry_telefono.grid(row=2, column=1, padx=10, pady=5)

        self.label_forma_pago = Label(self.root, text="Forma de Pago:")
        self.label_forma_pago.grid(row=3, column=0, padx=10, pady=5)
        self.entry_forma_pago = Entry(self.root)
        self.entry_forma_pago.grid(row=3, column=1, padx=10, pady=5)

        self.label_plazo_entrega = Label(self.root, text="Plazo de Entrega:")
        self.label_plazo_entrega.grid(row=4, column=0, padx=10, pady=5)
        self.entry_plazo_entrega = Entry(self.root)
        self.entry_plazo_entrega.grid(row=4, column=1, padx=10, pady=5)

        # Botones para operaciones CRUD
        self.btn_agregar = Button(self.root, text="Agregar", command=self.agregar_proveedor)
        self.btn_agregar.grid(row=5, column=0, padx=10, pady=5)

        self.btn_listar = Button(self.root, text="Listar", command=self.listar_proveedores)
        self.btn_listar.grid(row=5, column=1, padx=10, pady=5)

        # Texto y barra de desplazamiento para mostrar la lista de proveedores
        self.texto_proveedores = Text(self.root, width=60, height=10)
        self.texto_proveedores.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        self.scrollbar = Scrollbar(self.root, command=self.texto_proveedores.yview)
        self.scrollbar.grid(row=6, column=2, sticky='nsew')
        self.texto_proveedores.config(yscrollcommand=self.scrollbar.set)

    def agregar_proveedor(self):
        nombre = self.entry_nombre.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()
        forma_pago = self.entry_forma_pago.get()
        plazo_entrega = self.entry_plazo_entrega.get()

        if nombre and direccion and telefono and forma_pago and plazo_entrega:
            try:
                nuevo_proveedor = self.proveedor_controller.create_proveedor(nombre, direccion, telefono, forma_pago, plazo_entrega)
                messagebox.showinfo("Éxito", f"Proveedor {nuevo_proveedor.nombre} agregado exitosamente con ID: {nuevo_proveedor.id_proveedor}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el proveedor: {e}")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def listar_proveedores(self):
        try:
            proveedores = self.proveedor_controller.get_all_proveedores()
            if proveedores:
                self.texto_proveedores.delete(1.0, "end")
                for proveedor in proveedores:
                    self.texto_proveedores.insert("end", f"ID: {proveedor.id_proveedor}, Nombre: {proveedor.nombre}, Dirección: {proveedor.direccion}, Teléfono: {proveedor.telefono}, Forma de Pago: {proveedor.forma_pago}, Plazo de Entrega: {proveedor.plazo_entrega}\n")
            else:
                messagebox.showinfo("Información", "No hay proveedores registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar los proveedores: {e}")

    def iniciar(self):
        self.root.mainloop()

