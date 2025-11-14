#15 Suponga que tiene usted una tienda y desea registrar las ventas en una computadora. Diseñe un algoritmo en pseudocódigo que lea por cada cleinte:
# -El monto de la venta, calcule e imprima el IVA.
# -Calcule e imprima el total a pagar.
# -Lea la cantidad con la que paga el cliente (Solo efectivo), calcule e imprima el cambio. 

IVA = 0.19 #19%
Monto_Venta = float(input("Ingrese el monto de la venta: $"))
Total_Pagar = Monto_Venta * (1 + IVA)
print(f"IVA ({IVA*100:.0f}%): ${Monto_Venta * IVA:.2f}")
print(f"Total a pagar: ${Total_Pagar:.2f}")

Pago_Cliente = float(input("Ingrese la cantidad pagada (Efectivo): $"))
Cambio = Pago_Cliente - Total_Pagar
print(f"Cambio: ${Cambio:.2f}")
