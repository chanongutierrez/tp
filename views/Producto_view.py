from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, messagebox
from tkinter.ttk import Treeview
from controllers.Producto_controller import ProductoController

class ProductoView:
    def __init__(self, sql_manager):
        self.root = Tk()
        self.root.title("Gestión de Productos")
        self.producto_controller = ProductoController(sql_manager)

        # Etiquetas y campos de entrada para agregar productos
        self.label_nombre = Label(self.root, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = Entry(self.root)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        self.label_descripcion = Label(self.root, text="Descripción:")
        self.label_descripcion.grid(row=1, column=0, padx=10, pady=5)
        self.entry_descripcion = Entry(self.root)
        self.entry_descripcion.grid(row=1, column=1, padx=10, pady=5)

        self.label_precio_compra = Label(self.root, text="Precio de Compra:")
        self.label_precio_compra.grid(row=2, column=0, padx=10, pady=5)
        self.entry_precio_compra = Entry(self.root)
        self.entry_precio_compra.grid(row=2, column=1, padx=10, pady=5)

        self.label_precio_venta = Label(self.root, text="Precio de Venta:")
        self.label_precio_venta.grid(row=3, column=0, padx=10, pady=5)
        self.entry_precio_venta = Entry(self.root)
        self.entry_precio_venta.grid(row=3, column=1, padx=10, pady=5)

        # Agregar las etiquetas y campos de entrada restantes para los datos faltantes del producto
        self.label_categoria = Label(self.root, text="Categoría:")
        self.label_categoria.grid(row=4, column=0, padx=10, pady=5)
        self.entry_categoria = Entry(self.root)
        self.entry_categoria.grid(row=4, column=1, padx=10, pady=5)

        self.label_marca = Label(self.root, text="Marca:")
        self.label_marca.grid(row=5, column=0, padx=10, pady=5)
        self.entry_marca = Entry(self.root)
        self.entry_marca.grid(row=5, column=1, padx=10, pady=5)

        self.label_fecha_vencimiento = Label(self.root, text="Fecha de Vencimiento:")
        self.label_fecha_vencimiento.grid(row=6, column=0, padx=10, pady=5)
        self.entry_fecha_vencimiento = Entry(self.root)
        self.entry_fecha_vencimiento.grid(row=6, column=1, padx=10, pady=5)

        self.label_stock_minimo = Label(self.root, text="Stock Mínimo:")
        self.label_stock_minimo.grid(row=7, column=0, padx=10, pady=5)
        self.entry_stock_minimo = Entry(self.root)
        self.entry_stock_minimo.grid(row=7, column=1, padx=10, pady=5)

        self.label_unidad_medida = Label(self.root, text="Unidad de Medida:")
        self.label_unidad_medida.grid(row=8, column=0, padx=10, pady=5)
        self.entry_unidad_medida = Entry(self.root)
        self.entry_unidad_medida.grid(row=8, column=1, padx=10, pady=5)

        self.label_tipo = Label(self.root, text="Tipo:")
        self.label_tipo.grid(row=9, column=0, padx=10, pady=5)
        self.entry_tipo = Entry(self.root)
        self.entry_tipo.grid(row=9, column=1, padx=10, pady=5)

        # Botones para operaciones CRUD
        self.btn_agregar = Button(self.root, text="Agregar", command=self.agregar_producto)
        self.btn_agregar.grid(row=10, column=0, padx=10, pady=5)

        self.btn_listar = Button(self.root, text="Listar", command=self.listar_productos)
        self.btn_listar.grid(row=10, column=1, padx=10, pady=5)

        # Texto y barra de desplazamiento para mostrar la lista de productos
        self.texto_productos = Text(self.root, width=60, height=10)
        self.texto_productos.grid(row=11, column=0, columnspan=2, padx=10, pady=5)
        self.scrollbar = Scrollbar(self.root, command=self.texto_productos.yview)
        self.scrollbar.grid(row=11, column=2, sticky='nsew')
        self.texto_productos.config(yscrollcommand=self.scrollbar.set)

    def agregar_producto(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        precio_compra = self.entry_precio_compra.get()
        precio_venta = self.entry_precio_venta.get()
        categoria = self.entry_categoria.get()
        marca = self.entry_marca.get()
        fecha_vencimiento = self.entry_fecha_vencimiento.get()
        stock_minimo = self.entry_stock_minimo.get()
        unidad_medida = self.entry_unidad_medida.get()
        tipo = self.entry_tipo.get()

        if nombre and descripcion and precio_compra and precio_venta and categoria and marca and fecha_vencimiento and stock_minimo and unidad_medida and tipo:
            try:
                nuevo_producto = self.producto_controller.create_producto(nombre, descripcion, precio_compra, precio_venta, categoria, marca, fecha_vencimiento, stock_minimo, unidad_medida, tipo)
                messagebox.showinfo("Éxito", f"Producto {nuevo_producto.nombre} agregado exitosamente con ID: {nuevo_producto.id_producto}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el producto: {e}")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def listar_productos(self):
        try:
            productos = self.producto_controller.get_all_productos()
            if productos:
                self.texto_productos.delete(1.0, "end")
                for producto in productos:
                    self.texto_productos.insert("end", f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, Precio de Venta: {producto.precio_venta}\n")
            else:
                messagebox.showinfo("Información", "No hay productos registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar los productos: {e}")

    def iniciar(self):
        self.root.mainloop()

