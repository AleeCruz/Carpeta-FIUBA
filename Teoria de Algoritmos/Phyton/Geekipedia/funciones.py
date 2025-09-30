print("Vamos a ver sobre las funciones en python ")

def sumar_numero(n):
    print(n+3)
    
sumar_numero(7)

print("Tabla de multiplicar")

#Vamos a realizar la tabal de multiplicar para nuestro ejercicio
def multiplicacion(n):
    for i in range(1,11):
        print(n,"*",i,"=",i*n)
        
        
print("\nLa multiplicacion es: \n")
multiplicacion(8)
print("\nLa multiplicacion es: \n")
multiplicacion(5)


#Vamos a ver otro tipo de aplicaciones para las funciones
def dato():
    n = 2
    print(n)
    
dato()
dato()

m= 4
print(m)



#Vamosa ver sobre las funciones y su retorno de un determinado valor 
def resta(a,b):
    return a-b

resultado = resta(10,5)

print(resultado)
#Ejemplo de numeor pares e impares de numeros 

ejemplo = [4,6,7,5,3,6,8,2,56,1]

def separar_lista(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0: 
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

pares,impares = separar_lista(ejemplo)

print(pares)
print(impares)