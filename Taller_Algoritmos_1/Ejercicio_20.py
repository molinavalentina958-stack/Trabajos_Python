#20 Ingresar el precio de compra unitario de un producto y la cantidad de compra de dicho producto y un descuento. Calcular y mostrar el subtotal, el monto del IVA que es el 19% del subtotal, y el precio neto (Precio parcial con el monto del IVA).

IVA = 0.19
Producto = input("¿Producto que desea comprar?: ")
Precio = float(input("Precio unitario: $"))
Cantidad = int(input("Cantidad a comprar: "))
Descuento = float(input("Descuento (%): "))
Subtotal_con_Descuento = (Precio * Cantidad) * (1 - Descuento / 100)

print(f"\nProducto: {Producto}")
print(f"Subtotal con descuento sin IVA: ${Subtotal_con_Descuento:.2f}")
print(f"Monto del IVA (19%): ${Subtotal_con_Descuento * IVA:.2f}")
print(f"Precio Neto: ${Subtotal_con_Descuento * (1 + IVA):.2f}")
