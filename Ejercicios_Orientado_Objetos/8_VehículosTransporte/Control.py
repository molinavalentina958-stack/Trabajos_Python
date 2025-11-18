from VehiculoTerrestre import VehiculoTerrestre
from VehiculoAcuatico import VehiculoAcuatico

def control():
    auto = VehiculoTerrestre("Toyota", "Corolla", 5, 4)
    barco = VehiculoAcuatico("Yamaha", "WaveRunner", 3, "Motor fuera de borda")

    auto.mover()
    auto.frenar()
    print()

    barco.mover()
    barco.anclar()

control()