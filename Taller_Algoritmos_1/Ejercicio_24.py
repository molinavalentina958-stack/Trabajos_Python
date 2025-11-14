#24 Un estudiante realiza un préstamo a un plazo de 5 años, donde la tasa fija de interés es del 5% anual, se debe solicitar el monto del préstamo y desea calcular la siguiente información: 
# -Cuanto dinero se ha pagado de intereses en un año.
# -Cuanto dinero se ha pagado de intereses en el tercer trimestre del año.
# -Cuanto dinero se ha pagado de intereses en el primer mes. 
# -Cuanto dinero se paga en total del préstamo solicitado incluyendo intereses.

Tasa_Anual = 0.05
Plazo = 5
Monto = float(input("Ingrese el monto del préstamo: $"))
Interes_Anual = Monto * Tasa_Anual
print(f"Monto préstamo: ${Monto:.2f} | Tasa: {Tasa_Anual*100:.0f}% | Plazo: {Plazo} años")
print(f"Intereses en 1 año: ${Interes_Anual:.2f}")
print(f"Intereses en el 3 trimestre: ${Interes_Anual/4:.2f}")
print(f"Intereses en el 1 mes: ${Interes_Anual/12:.2f}")

Total_Pagar = Monto + (Interes_Anual * Plazo)
print(f"Total a pagar (Intereses): ${Total_Pagar:.2f}")
