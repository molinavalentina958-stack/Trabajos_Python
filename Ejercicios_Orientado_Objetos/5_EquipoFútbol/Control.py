from Jugador import Jugador 
from Equipo import Equipo

def control():
    equipo1 = Equipo("Atlético Nacional", "Medellín", "DT Bodmer")
    jugador1 = Jugador("Jefferson", "Delantero", 23, 9)
    jugador2= Jugador("Sebastián", "Defensa", 27, 4)

    equipo1.agregar(jugador1)
    equipo1.agregar(jugador2)
    equipo1.mostrar()

control()