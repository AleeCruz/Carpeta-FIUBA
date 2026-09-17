notas_alumnos = [("Carlos", 8), ("Sofia", 4), ("Mateo", 10), ("Elena", 5)]

#Debemos de realizar un for para que recorra las lista e imprima solo
#A aquellos que tengan una nota mayor a 6


#Realizando el for 
for elemento in notas_alumnos:
    if elemento[1]>6:
        print(elemento[0]," aprobo con ",elemento[1])
