#6 Lea la cantidad de dinero correspondiente a una compra y calcule el valor del IVA (19%) y el valor total de la factura, si al valor de la compra se le autoriza un descuento del 10% (Antes de aplicarle el IVA).

Valor_Compra = float(input("Valor total de la compra: "))
Opción_Descuento = input("¿Aplica descuento del 10%?\nMarque 1 para Sí, 2 para No: ")

if Opción_Descuento == "1":
    subtotal = Valor_Compra - (Valor_Compra * 0.90)
else:
    subtotal = Valor_Compra

Valor_Total_Factura = subtotal + (subtotal * 1.19)

print("-" * 30)
print(f"Subtotal (con/sin descuento): ${subtotal:.2f}")
print(f"Valor total de la factura: ${Valor_Total_Factura:.2f}")
print("-" * 30)
