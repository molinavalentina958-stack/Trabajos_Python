#14 Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de varios artículos (4) determinados, del que se adquieren una o varias unidades. El IVA es del 19%.

Subtotal = (int(input("Unidades de Tomate ($5000): ")) * 5000) + (int(input("Unidades de Papa ($3000): ")) * 3000) + (int(input("Unidades de Lechuga ($2500): ")) * 2500) + (int(input("Unidades de Cebolla ($1500): ")) * 1500)    

print(f"Subtotal (Sin IVA): ${Subtotal:,.2f}")
print(f"IVA (19%): ${Subtotal * 0.19:,.2f}")
print(f"Total a Pagar: ${Subtotal * 1.19:,.2f}")
