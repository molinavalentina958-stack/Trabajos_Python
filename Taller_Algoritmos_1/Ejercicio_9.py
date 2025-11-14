#9 Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

Sueldo_Base = float(input("Ingrese el sueldo base: "))
Total_Ventas = float(input("Valor venta 1:")) + float(input("Valor venta 2:")) + float(input("Valor venta 3:"))
Comisión = Total_Ventas * 0.10
Total_a_recibir = Sueldo_Base + Comisión

print("\n" + "=" * 35)
print(f"Comisión por ventas: ${Comisión:.2f}")
print(f"Total a recibir: ${Total_a_recibir:.2f}")
print("=" * 35)
