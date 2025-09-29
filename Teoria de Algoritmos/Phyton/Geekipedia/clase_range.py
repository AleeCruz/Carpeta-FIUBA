#Vamos a ver la clase range genera un rango de números enteros, nos
#permite trabajar con un ranog de un minimo y un maximo 
"""
La clase range puede trabajr con un unico argumento renge(stop)
La clase range puede trabajar con dos argumentos range(start,stop)
La clase range tambien puede trabajar con tres argumentos range (start, stop,step)"""
#Opcion1
#Range(stop)
#La funcion range con un solo argumento siempre trabajara con el valor 0 como unico
#Argumento, y el valor trabaja hasta que llegue al stop pero nunca toma el ultimo valor 
#Suponiendo que tengamos range(7) se generara una secuencia comenzando en 
#0 1 2 3 4 5 6 
#range(5,11) , la funcion rrange comenzara en 5  y se generara una secuencia numerica desde 
# 5 6 7 8 9 10
#Suponiendo que tengamos un range(2,6) 2 3 4 5 seran los valores que se generaran

#Opcion 3 cuando range toma tres argumentos range(start,stop,step)
#range(0,11,2) los valores se generaran desde 0 hasta 10 pero con pasos de 
#dos en dos 0 2 4 6 8 10

#Opcion 3
#range (5,21,5) los valores que se generan son 5 10 15 y 20 

#Opcion4 
#Hay una peculiaridad donde podemos aplicar range desde range(10,0) no hace nada
#en cambio si quisieramos un decrecimineto del tipo 10 9 8 7 6 .....1

#En casos como estos podriamos aplicar lo siguiente
#range(10,0,-1) el decrecimiento funcionaria de 1 en 1 decrementandolo

