from Cliente import Cliente
from Producto import Producto
from Pedido import Pedido

cliente1 = Cliente("Valentina", "vale@gmail.com", 312456789)
producto1 = Producto(102, "Celular", 1800000)
producto2 = Producto(103, "Computador", 3500000)
pedido = Pedido(cliente1, "2025-11-18")

pedido.agregarProducto(producto1)
pedido.agregarProducto(producto2)

print("Cliente:", pedido.get_cliente().get_nombre())
print("Fecha:", pedido.get_fecha())
print("Total:", pedido.get_total())

print("Productos:")
for prod in pedido.get_productos():
    print("-", prod.get_nombre(), "$", prod.get_precio())