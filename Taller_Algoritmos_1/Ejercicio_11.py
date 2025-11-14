#11 Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

print("Ingrese las 3 notas de los parciales:")
Suma_Parciales = float(input("Nota Parcial 1: ")) + float(input("Nota Parcial 2: ")) + float(input("Nota Parcial 3: "))
Examen_Final = float(input("Ingrese la nota del Examen Final (30%): "))
Trabajo_Final = float(input("Ingrese la nota del Trabajo Final (15%): "))
Calificacion_Final = (Suma_Parciales / 3 * 0.55) + (Examen_Final * 0.30) + (Trabajo_Final * 0.15)

print(f"Su calificación final es: {Calificacion_Final:.2f}")
