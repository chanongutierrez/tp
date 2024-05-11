from views.Producto_view import ProductoView
from views.Cliente_view import ClienteView
from views.Proveedor_view import ProveedorView
from views.Deposito_view import DepositoView
from views.Sucursal_view import SucursalView
from views.MovimientoInventario_view import MovimientoInventarioView

class ViewFactory:
    @staticmethod
    def create_view(view_name, master, sql_manager):
        if view_name == "Productos":
            return ProductoView(sql_manager)
        elif view_name == "Clientes":
            return ClienteView(sql_manager)
        elif view_name == "Proveedores":
            return ProveedorView(sql_manager)
        elif view_name == "Depósitos":
            return DepositoView(sql_manager)
        elif view_name == "Sucursales":
            return SucursalView(sql_manager)
        elif view_name == "Movimientos de Inventario":
            return MovimientoInventarioView(sql_manager)
        else:
            raise ValueError(f"Vista '{view_name}' no encontrada.")
