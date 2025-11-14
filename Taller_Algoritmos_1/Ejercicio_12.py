#12 Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de alumnos.

Mujeres = int(input("Ingrese la cantidad de mujeres en el grupo: "))
Hombres = int(input("Ingrese la cantidad de hombres en el grupo: "))
print(f"El porcentaje de mujeres en el grupo es: {(Mujeres/(Mujeres + Hombres)) * 100}%")
print(f"El porcentaje de hombres en el grupo es: {(Hombres/(Mujeres + Hombres)) * 100}%")
