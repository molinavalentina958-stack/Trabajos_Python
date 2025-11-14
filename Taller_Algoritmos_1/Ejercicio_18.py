#18 En una universidad los estudiantes pueden pagar el valor de su matrícula en cuatro cuotas de la siguiente forma: 
# -Primera cuota: 40%.
# -Segunda cuota: 25%.
# -Tercera cuota: 20%.
# -Cuarta cuota: 15%.
# Diga cuanto es el valor que tiene que pagar por cuota un estudiante.

Valor_Matrícula = float(input("Ingrese el valor de la matrícula: $"))
Primera_Cuota = Valor_Matrícula * 0.40
Segunda_Cuota = Valor_Matrícula * 0.25
Tercera_Cuota = Valor_Matrícula * 0.20
Cuarta_Cuota = Valor_Matrícula * 0.15

print(f"Valor de la primera cuota (40%): ${Primera_Cuota:.2f}")
print(f"Valor de la segunda cuota (25%): ${Segunda_Cuota:.2f}")
print(f"Valor de la tercera cuota (20%): ${Tercera_Cuota:.2f}")
print(f"Valor de la cuarta cuota (15%): ${Cuarta_Cuota:.2f}")
print(f"Valor a pagar en total: ${Primera_Cuota + Segunda_Cuota + Tercera_Cuota + Cuarta_Cuota:.2f}")
