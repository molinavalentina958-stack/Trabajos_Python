#4 Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura si la primera nota tiene un valor del 20%, la segunda del 30% y la última del 50%.

Definitiva = (3*0.20) + (4*0.30) + (5*0.50)

Nota1 = float(input("Ingrese la primera nota: "))
Nota2 = float(input("Ingrese la segunda nota: "))
Nota3 = float(input("Ingrese la tercera nota: "))

print(f"La nota definitiva del aprendiz es: {(Nota1*0.20) + (Nota2*0.30) + (Nota3*0.50)}")
