#7 Dada una cantidad de tiempo medida en horas, minutos y segundos, diga a cuántos segundos equivale.

Horas = int(input("Ingrese la cantidad de horas: "))
Minutos = int(input("Ingrese la cantidad de minutos: "))
Segundos = int(input("Ingrese la cantidad de segundos: "))

Segundos_de_Horas = Horas * 3600
Segundos_de_Minutos = Minutos * 60
Segundos_directos = Segundos
Total_Segundos = Segundos_de_Horas + Segundos_de_Minutos + Segundos_directos

print(f"La cantidad total de segundos es: {Total_Segundos} segundos")
