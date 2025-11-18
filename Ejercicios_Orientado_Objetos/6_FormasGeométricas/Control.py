from Circulo import Circulo
from Rectangulo import Rectangulo

def control():
    forma1 = Circulo("Morado", 5)
    forma2 = Rectangulo("Rosado", 12, 8)

    formas = [forma1, forma2]

    for f in formas: 
        f.mostrar_informacion()

control()