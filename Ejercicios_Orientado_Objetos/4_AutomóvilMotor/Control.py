from Motor import Motor
from Automovil import Automovil

def control():
    motor1 = Motor(5000, "Gasolina", 460)
    auto1 = Automovil("Ford", "Mustang GT", 2020, "Negro", motor1)

    auto1.get_info()
    auto1.encender()
    auto1.acelerar()
    auto1.apagar()

control()