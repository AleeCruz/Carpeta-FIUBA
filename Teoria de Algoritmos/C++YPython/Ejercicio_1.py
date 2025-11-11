

paciente_1 = float (input("Ingrese la presion del paciente 1: "))
paciente_2 = float (input("Ingrese la presion del paciente 2: "))
paciente_3 = float (input("Ingrese la presion del paciente 3: "))

promedio = (paciente_1 + paciente_2 + paciente_3) / 3


if promedio < 110:
    print("Presion baja")
elif promedio >= 110 and promedio <= 130:
    print("Presion normal")
else:
    print("Presion alta")