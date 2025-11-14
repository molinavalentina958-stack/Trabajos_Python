#21 Realice un algoritmo que permita realizar el cálculo del siguiente enunciado, se solicita el año de nacimiento del aprendiz, el nombre, la dirección, se requiere conocer la edad de la persona y la información completa ingresada.

Año_Actual = 2025 
Año_Nacimiento = int(input("Ingrese su año de nacimiento (AAAA): "))
Nombre = input("Ingrese su nombre completo: ")
Direccion = input("Ingrese su dirección: ")
Edad = Año_Actual - Año_Nacimiento

print("---Información del aprendiz:---")
print(f"Nombre: {Nombre}")
print(f"Dirección: {Direccion}")
print(f"Edad: {Edad} años")
