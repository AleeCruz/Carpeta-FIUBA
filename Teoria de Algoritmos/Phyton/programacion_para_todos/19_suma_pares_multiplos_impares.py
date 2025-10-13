print("Programa que sumen los pares y multiplique los impares")

suma =0
multiplicacion =1
numero = 1

while numero !=0:
    numero = int(input("Ingrese un numero (presione la tecla 0 para salir): "))
    
    if numero != 0:
        
        if numero % 2 == 0:
            suma = suma + numero
        else:
            multiplicacion *= numero
    
print(f"La suma de los numeros pares es: {suma}")
print(f"La multiplicacion de los numeros impares es: {multiplicacion}")