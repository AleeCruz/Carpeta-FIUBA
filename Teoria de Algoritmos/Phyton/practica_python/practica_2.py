nota = int(input("Ingresa la nota del estudiante: "))

#Evaluacion de las condiciones de la nota del estudiante

if nota < 4:
    print("Insuficiente")
elif nota <= 6:
    print("Aprobado")
elif nota <= 9:
    print("Muy bien")
else:
    print("Excelente")

    