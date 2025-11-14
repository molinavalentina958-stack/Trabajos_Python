#17 Desarrollar un algoritmo que permita generar la colilla de pago de los empleados de una empresa. La colilla debe mostrar:
# -El salario del empleado.
# -El valor de ahorro mensual programado. 
# -La suma a deducir por aporte a la salud (EPS) 12,5%.
# -La suma a deducir por aporte al fondo de pensiones 16%.
# -Total a recibir.
# -Toda la información que debe proveer el usuario del programa es el salario del empleado y el valor de ahorro mensual programado. El programa debe calcular y devolver el resto de los datos.

Salud = 0.125 
Pensión = 0.16 
Salario = float(input("Ingrese el salario del empleado: $"))
Ahorro_Valor = float(input("Ingrese el valor de ahorro mensual programado: $"))
Deducción_Salud = Salario * Salud
Deducción_Pensión = Salario * Pensión
Total_Deducción = Ahorro_Valor + Deducción_Salud + Deducción_Pensión
Total_Recibir = Salario - Total_Deducción

print("-----Colilla de Pago Mensual----")
print(f"Salario base: ${Salario:.2f}")
print("Deducciones:")
print(f"Ahorro programado: ${Ahorro_Valor:.2f}")
print(f"Aporte por salud (12.5%): ${Deducción_Salud:.2f}")
print(f"Aporte por fondo de pensión (16%): ${Deducción_Pensión:.2f}")
print(f"Total a recibir: ${Total_Deducción:.2f}")
