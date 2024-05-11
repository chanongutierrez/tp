from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, messagebox
from tkinter.ttk import Treeview
from controllers.Cliente_controller import ClienteController

class ClienteView:
    def __init__(self, sql_manager):
        self.root = Tk()
        self.root.title("Gestión de Clientes")
        self.cliente_controller = ClienteController(sql_manager)

        # Etiquetas y campos de entrada para agregar clientes
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

        # Botones para operaciones CRUD
        self.btn_agregar = Button(self.root, text="Agregar", command=self.agregar_cliente)
        self.btn_agregar.grid(row=3, column=0, padx=10, pady=5)

        self.btn_listar = Button(self.root, text="Listar", command=self.listar_clientes)
        self.btn_listar.grid(row=3, column=1, padx=10, pady=5)

        self.btn_actualizar = Button(self.root, text="Actualizar", command=self.actualizar_cliente)
        self.btn_actualizar.grid(row=3, column=2, padx=10, pady=5)

        self.btn_eliminar = Button(self.root, text="Eliminar", command=self.eliminar_cliente)
        self.btn_eliminar.grid(row=3, column=3, padx=10, pady=5)

        # Texto y barra de desplazamiento para mostrar la lista de clientes
        self.texto_clientes = Text(self.root, width=60, height=10)
        self.texto_clientes.grid(row=4, column=0, columnspan=4, padx=10, pady=5)
        self.scrollbar = Scrollbar(self.root, command=self.texto_clientes.yview)
        self.scrollbar.grid(row=4, column=4, sticky='nsew')
        self.texto_clientes.config(yscrollcommand=self.scrollbar.set)

        # Variable para almacenar el cliente seleccionado
        self.cliente_seleccionado = None

    def agregar_cliente(self):
        nombre = self.entry_nombre.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()

        if nombre and direccion and telefono:
            try:
                if self.cliente_seleccionado:
                    # Si hay un cliente seleccionado, se trata de una actualización
                    cliente_id = self.cliente_seleccionado['values'][0]
                    self.cliente_controller.update_cliente(cliente_id, nombre, direccion, telefono)
                    messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
                else:
                    nuevo_cliente = self.cliente_controller.create_cliente(nombre, direccion, telefono)
                    messagebox.showinfo("Éxito", f"Cliente {nuevo_cliente.nombre} agregado exitosamente con ID: {nuevo_cliente.id_cliente}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar o actualizar el cliente: {e}")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def listar_clientes(self):
        try:
            clientes = self.cliente_controller.get_all_clientes()
            if clientes:
                self.texto_clientes.delete(1.0, "end")
                for cliente in clientes:
                    self.texto_clientes.insert("end", f"ID: {cliente.id_cliente}, Nombre: {cliente.nombre}, Dirección: {cliente.direccion}, Teléfono: {cliente.telefono}\n")
            else:
                messagebox.showinfo("Información", "No hay clientes registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar los clientes: {e}")

    def actualizar_cliente(self):
        # Obtener el cliente seleccionado desde el texto
        cliente_seleccionado_index = self.texto_clientes.index("sel.first")
        cliente_seleccionado_info = self.texto_clientes.get(cliente_seleccionado_index.split(".")[0] + ".0", cliente_seleccionado_index)
        cliente_id = cliente_seleccionado_info.split(",")[0].split(":")[1].strip()

        # Obtener los detalles del cliente desde la base de datos
        cliente = self.cliente_controller.get_cliente_by_id(cliente_id)

        # Actualizar los campos de entrada con los detalles del cliente seleccionado
        self.entry_nombre.delete(0, "end")
        self.entry_nombre.insert(0, cliente.nombre)
        self.entry_direccion.delete(0, "end")
        self.entry_direccion.insert(0, cliente.direccion)
        self.entry_telefono.delete(0, "end")
        self.entry_telefono.insert(0, cliente.telefono)

        # Actualizar la variable de cliente seleccionado
        self.cliente_seleccionado = cliente_seleccionado_info

    def eliminar_cliente(self):
        if self.cliente_seleccionado:
            cliente_id = self.cliente_seleccionado['values'][0]
            confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este cliente?")
            if confirmacion:
                try:
                    self.cliente_controller.delete_cliente(cliente_id)
                    messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo eliminar el cliente: {e}")
        else:
            messagebox.showerror("Error", "Por favor seleccione un cliente para eliminar.")

    def iniciar(self):
        self.root.mainloop()

