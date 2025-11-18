from Animales import Animales
from Mamiferos import Mamiferos
from Aves import Aves
from Cuidador import Cuidador
from Jaula import Jaula

def control():
    leon = Mamiferos("León", 5, "Felino", "Melena densa")
    loro = Aves("Loro", 2, "Ave tropical", "Alas verdes")
    cuidador1 = Cuidador("Carlos", 8)

    jaula1 = Jaula()
    jaula1.asignarCuidador(cuidador1)
    jaula1.asignarAnimal(leon)
    jaula1.asignarAnimal(loro)

    leon.hacer_sonido()
    leon.amamantar()
    loro.volar()

control()