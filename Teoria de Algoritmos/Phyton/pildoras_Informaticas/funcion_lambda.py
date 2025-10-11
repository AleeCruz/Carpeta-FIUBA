"""Vamos a ver osbre las funciones lambda que son funciones anonimas 
se la conoce tambie como funciones
on the go 
on demand
online"""

area_triangulo = lambda base,altura: (base*altura)/2

triangulo = area_triangulo(3,6)

print(triangulo)


#Vamos a ver otro ejempo de funciones lambda 

al_cubo = lambda numero: numero**3
print(al_cubo(3))
print("Otra forma de ver el funcionamiento de lambda es:")

al_cubo_2 = lambda numero: pow(numero,2)
print(al_cubo_2(3))