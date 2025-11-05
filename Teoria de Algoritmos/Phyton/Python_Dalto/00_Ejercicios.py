"""Se estan por realizar las elecciones nacionales en Madagascar, se necesita un programa de software
que permita registrar los votos de los ciudadanos, se necesita saber la cantidad total de votos para 
cada candidato, los candidatos disponibles son "A", "B", "C","D" y "E". El programa debe finalizar 
cuando el encargado de las elecciones lo decida."""

"""Ahora se decide ingresar el nombre y la edad de cada votante, aunque se necesita saber 
el candidato mas viejo y su nombre que voto al candidato E"""

nombre = ""
edad = 0
edad_veterano = 0
nombre_veterano = ""

candidato_elegido = ""

condicion_bucle = "S"

cantidad_votos_A = 0
cantidad_votos_B = 0
cantidad_votos_C = 0
cantidad_votos_D = 0
cantidad_votos_E = 0

while condicion_bucle == "S":
    

    print("\n")
    nombre = input("Ingresa tu nombre: ")
    edad = int(input ("Ingresa tu edad: "))
    
    candidato_elegido = input("Ingrese el candidato elegido (A-B-C-D-E): ")
    match candidato_elegido:
        case "A":
            cantidad_votos_A += 1
        case "B":
            cantidad_votos_B += 1
        case "C":
            cantidad_votos_C += 1
        case "D":
            cantidad_votos_D += 1
        case "E":
            cantidad_votos_E += 1
            if edad > edad_veterano:
                edad_veterano = edad
                nombre_veterano = nombre
            
            
    condicion_bucle = input("Deseas continuar con las elecciones (S-N): ")
    

print("Cantidad de votos para el candidato A: ", cantidad_votos_A)
print("Cantidad de votos para el candidato B: ", cantidad_votos_B)
print("Cantidad de votos para el candidato C: ", cantidad_votos_C)
print("Cantidad de votos para el candidato D: ", cantidad_votos_D)
print("Cantidad de votos para el candidato E: ", cantidad_votos_E)

print("El nombre del votante mas viejo que voto al candidato E es: ", nombre_veterano)
print("La edad del votante mas viejo que voto al candidato E es: ", edad_veterano)
