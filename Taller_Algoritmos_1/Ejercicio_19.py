#19 Ingresar, para un estudiante, sus 5 notas de un curso, nombre, programa, ficha.
# Hacer un algoritmo que:
# -Muestre el nombre.
# -Muestre el programa de formación. 
# Se debe calcular y mostrar su promedio final.

Nombre = input("Ingrese el nombre del estudiante: ")
Programa = input("Ingrese el programa de formación: ")
Ficha = input("Ingrese el número de ficha: ")

print("\n--- Ingrese las 5 notas ---")

Suma_Notas = float(input("Ingrese la nota 1: ")) + float(input("Ingrese la nota 2: ")) + float(input("Ingrese la nota 3: ")) + float(input("Ingrese la nota 4: ")) + float(input("Ingrese la nota 5: "))
print("\n--- Datos del Estudiante ---")
print(f"Nombre: {Nombre}")
print(f"Programa: {Programa}")
print(f"Ficha: {Ficha}")
print(f"Promedio Final: {(Suma_Notas / 5):.2f}")
