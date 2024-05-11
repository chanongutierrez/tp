from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, messagebox
from controllers.MovimientoInventario_controller import MovimientoInventarioController
from models.SQLmanager import SQLManager

class MovimientoInventarioView:
    def __init__(self, sql_manager):
        self.root = Tk()
        self.root.title("Gestión de Movimientos de Inventario")
        self.movimiento_controller = MovimientoInventarioController(sql_manager)

        # Etiquetas y campos de entrada para agregar movimientos de inventario
        self.label_producto = Label(self.root, text="Producto:")
        self.label_producto.grid(row=0, column=0, padx=10, pady=5)
        self.entry_producto = Entry(self.root)
        self.entry_producto.grid(row=0, column=1, padx=10, pady=5)

        self.label_cantidad = Label(self.root, text="Cantidad:")
        self.label_cantidad.grid(row=1, column=0, padx=10, pady=5)
        self.entry_cantidad = Entry(self.root)
        self.entry_cantidad.grid(row=1, column=1, padx=10, pady=5)

        self.label_tipo = Label(self.root, text="Tipo:")
        self.label_tipo.grid(row=2, column=0, padx=10, pady=5)
        self.entry_tipo = Entry(self.root)
        self.entry_tipo.grid(row=2, column=1, padx=10, pady=5)

        # Botones para operaciones CRUD
        self.btn_agregar = Button(self.root, text="Agregar", command=self.agregar_movimiento)
        self.btn_agregar.grid(row=3, column=0, padx=10, pady=5)

        self.btn_listar = Button(self.root, text="Listar", command=self.listar_movimientos)
        self.btn_listar.grid(row=3, column=1, padx=10, pady=5)

        # Texto y barra de desplazamiento para mostrar la lista de movimientos de inventario
        self.texto_movimientos = Text(self.root, width=60, height=10)
        self.texto_movimientos.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        self.scrollbar = Scrollbar(self.root, command=self.texto_movimientos.yview)
        self.scrollbar.grid(row=4, column=2, sticky='nsew')
        self.texto_movimientos.config(yscrollcommand=self.scrollbar.set)

    def agregar_movimiento(self):
        producto = self.entry_producto.get()
        cantidad = self.entry_cantidad.get()
        tipo = self.entry_tipo.get()

        if producto and cantidad and tipo:
            try:
                nuevo_movimiento = self.movimiento_controller.create_movimiento(producto, cantidad, tipo)
                messagebox.showinfo("Éxito", f"Movimiento de inventario agregado exitosamente con ID: {nuevo_movimiento.id_movimiento}")
                self.listar_movimientos()  # Actualiza la lista después de agregar un movimiento
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el movimiento de inventario: {e}")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def listar_movimientos(self):
        try:
            movimientos = self.movimiento_controller.get_all_movimientos()
            if movimientos:
                self.texto_movimientos.delete(1.0, "end")
                for movimiento in movimientos:
                    self.texto_movimientos.insert("end", f"ID: {movimiento.id_movimiento}, Producto: {movimiento.producto}, Cantidad: {movimiento.cantidad}, Tipo: {movimiento.tipo}\n")
            else:
                messagebox.showinfo("Información", "No hay movimientos de inventario registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar los movimientos de inventario: {e}")

    def iniciar(self):
        self.listar_movimientos()  # Muestra la lista de movimientos de inventario al iniciar la aplicación
        self.root.mainloop()


