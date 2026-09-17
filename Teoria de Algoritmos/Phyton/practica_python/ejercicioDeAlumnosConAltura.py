"""Se debe realizar un algoritmos quenos permita encontrar el menor de las alturas 
en un arreglo o listas de alturas que nos permita las siguientes definidsiones son necesairias 
"""



#Se debe crear una funcion que devuelva el que devuelva en tiempo logaritmico la alturas 
#De algunos de los alumnos con las siguientes caracteristicas

def indice_mas_bajo(alumnos):
    #Empezamos a inicializar las variables de inicio y fin del arreglo
    inicio =0
    fin = len (alumnos)-1#Me devuelve el tamaño del arreglo que estamos analizando
    while inicio <fin: """Debemos considerar el uso de un while que nos permita iterar 
    varias veces sobre una estructura en particular en cada while debemos
    de ṕartir el arreglo a la mitad"""


    mitad = (inicio + fin)//2 #Estamos dividiendo el arreglo a la mitad 
    #Por lo tanto la division se realizara como una division entera, o sea que 3.5 
    #en realizadad nos dejaria con 3 enteroa

    if alumnos[medio].altura > alumnos[medio+1].altura:
        inicio = medio + 1
    else
        fin = medio



    return return inicio

#Que tipo de estructura debemos de realizar para que este funcione???


"""Se debe de realizar un algoritmo que nos permita dividir el problema a la mitad,
es un tipico ejercicio de division y conquista

Tenemos lo siguiente un arreglo de alumnos con las siguientes caracteristicas 

alumnos = [
    Alumno("Ana", 1.2),
    Alumno("Bruno", 1.15),
    Alumno("Carlos", 1.14),
    Alumno("Daniela", 1.12),
    Alumno("Esteban", 1.02),
    Alumno("Felipe", 0.98),  # Alumno más bajo (índice 5)
    Alumno("Gabriela", 1.18),
    Alumno("Hugo", 1.23)
]
Suponiendo que estemos usando los datos de arriba, enotnces nuestro objetivo es
el recuento de cada uno de los elemeentos en nuestras variables de iinicio y fin

Tenemos en este caso 
inicio =0// denota el inicio del arreglo de la lista

fin = len(alumnos)-1//Hace referencia a la cnatidad de elementos que existen en 
el arreglo en esta caso son 8 elementos , pero como en todo arrelgo son solamente 0 a 7
elemento




debemosde recorrer alumno por alumno realizando un algoritmo de division y conquista basico 
que trata de una busqueda binaria 
"""





"""
En esta seccion del archivo vamos a realizar el algoritmos de busqueda binaria para 
un arreglo de 8 elementos 

 tenemos el siguiente arreglo, por lo tanto debemos de realizar una busqueda binaria 
 para obtener el indice mas bajo
[1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23]

entonces tenemos lo siguiente


def indice_mas_bajo(alumnos):  //Se le paso un arreglo de 7 elemeentos
    inicio =0}
    fin = len(alumnos)-1//devuelve la cantidad de 7 elementos 

    while inicio<fin:
        mitad = (inicio+fin//2 Esto nos dejara con un valor entero de 3 no es el caso de 3.5


vamos a realizar un condicional para preguntar por cada uni¿o de los elemenetos que estan 
apareciendo en la lista 




def indice_mas_bajo(alumnos):
    inci



Tendriamos lo siguiente 

"""

def indice_mas_bajo(alumnos):
    inicio =0
    fin = len(alumnos)-1 #medimos la cantidad de elementos que tiene el arreglo

    while inicio<fin:#Realizamos una iteracion por cada particion a la mitad que estemo realizando 
        
        mitad = (inicio + fin)//2

        if alumnos[mitad].altura > alumnos[mitad+1].altura
            incio = mitad
        else 
            fin = mitad +1
    return inicio
