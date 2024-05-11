from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, messagebox
from controllers.Sucursal_controller import SucursalController

class SucursalView:
    def __init__(self, sql_manager):
        self.root = Tk()
        self.root.title("Gestión de Sucursales")
        self.sucursal_controller = SucursalController(sql_manager)

        # Etiquetas y campos de entrada para agregar sucursales
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

        self.label_persona_cargo = Label(self.root, text="Persona a Cargo:")
        self.label_persona_cargo.grid(row=4, column=0, padx=10, pady=5)
        self.entry_persona_cargo = Entry(self.root)
        self.entry_persona_cargo.grid(row=4, column=1, padx=10, pady=5)

        # Botones para operaciones CRUD
        self.btn_agregar = Button(self.root, text="Agregar", command=self.agregar_sucursal)
        self.btn_agregar.grid(row=5, column=0, padx=10, pady=5)

        self.btn_listar = Button(self.root, text="Listar", command=self.listar_sucursales)
        self.btn_listar.grid(row=5, column=1, padx=10, pady=5)

        # Texto y barra de desplazamiento para mostrar la lista de sucursales
        self.texto_sucursales = Text(self.root, width=60, height=10)
        self.texto_sucursales.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        self.scrollbar = Scrollbar(self.root, command=self.texto_sucursales.yview)
        self.scrollbar.grid(row=6, column=2, sticky='nsew')
        self.texto_sucursales.config(yscrollcommand=self.scrollbar.set)

    def agregar_sucursal(self):
        nombre = self.entry_nombre.get()
        ubicacion = self.entry_ubicacion.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()
        persona_cargo = self.entry_persona_cargo.get()

        if nombre and ubicacion and direccion and telefono and persona_cargo:
            try:
                nueva_sucursal = self.sucursal_controller.create_sucursal(nombre, ubicacion, direccion, telefono, persona_cargo)
                messagebox.showinfo("Éxito", f"Sucursal {nueva_sucursal.nombre} agregada exitosamente con ID: {nueva_sucursal.id_sucursal}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar la sucursal: {e}")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def listar_sucursales(self):
        try:
            sucursales = self.sucursal_controller.get_all_sucursales()
            if sucursales:
                self.texto_sucursales.delete(1.0, "end")
                for sucursal in sucursales:
                    self.texto_sucursales.insert("end", f"ID: {sucursal.id_sucursal}, Nombre: {sucursal.nombre}, Ubicación: {sucursal.ubicacion}, Dirección: {sucursal.direccion}, Teléfono: {sucursal.telefono}, Persona a Cargo: {sucursal.persona_cargo}\n")
            else:
                messagebox.showinfo("Información", "No hay sucursales registradas.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar las sucursales: {e}")

    def iniciar(self):
        self.root.mainloop()

