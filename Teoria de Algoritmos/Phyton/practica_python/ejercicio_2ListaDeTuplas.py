carrito = [("Pan", 150, 2), ("Leche", 200, 3), ("Queso", 500, 1)]


#Dado una lista de tuplas nuestro objetivo es calcular el gasto total, al
#multiplicar precio por cantidad en cada elemento de la lista
total_gastado = 0

for elemento in carrito:
    total_gastado += elemento[1]*elemento[2]

print(total_gastado)

#Conclusion Funciona correctamente