class Automovil: 
    def __init__(self, marca, modelo, anio, color, motor):
        self._marca = marca 
        self._modelo = modelo 
        self._anio = anio 
        self._color = color
        self._motor = motor
        self._encendido = False

    def set_marca(self, marca):
        self._marca = marca
    
    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_anio(self, anio):
        self._anio = anio

    def set_color(self, color):
        self._color = color

    def set_motor(self, motor):
        self._motor = motor

    def get_marca(self):
        return self._marca
    
    def get_modelo(self):
        return self._modelo

    def get_anio(self):
        return self._anio

    def get_color(self):
        return self._color

    def get_motor(self):
        return self._motor
    
    def get_encendido(self):
        return self._encendido

    def encender(self):
        if not self._encendido:
            self._encendido = True
            print("El automóvil ha sido encendido.")
        else: 
            print("El automóvil ya estaba encendido.")

    def apagar(self):
        if self._encendido:
            self._encendido = False
            print("El automóvil ha sido apagado.")
        else: 
            print("El automóvil ya estaba apagado.")

    def acelerar(self):
        if self._encendido:
            print("El automóvil está acelerando.")
        else: 
            print("No se puede acelerar. El automóvil está apagado.")

    def get_info(self):
        print(f"""
Automóvil:
- Marca: {self._marca}
- Modelo: {self._modelo}
- Año: {self._anio}
- Color: {self._color}
- Motor: {self._motor.get_info()}
""")