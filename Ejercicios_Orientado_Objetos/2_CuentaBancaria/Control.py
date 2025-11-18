from Cuenta import Cuenta

def control_cuenta():
    cuenta = Cuenta (10293940593, "Valentina", 1000000, "15/11/2025", "Activa")

    cuenta.DepositarDinero(70000)
    cuenta.RetirarDinero(35000)
    cuenta.ConsultarDinero()
    
control_cuenta()