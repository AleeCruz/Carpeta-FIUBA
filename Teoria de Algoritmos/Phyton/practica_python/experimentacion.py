#Vamos a generar un arreglo/lista de monedas  para resolver el 
#problema del cambio 



def cambio(monedas,monto):
    monedas_ordenadas = sorted(monedas,reverse=True)
    monedas_usadas=[]
    i =len(monedas)-1
    while i >=0:
        print(monedas[i])
        if (monto//monedas[i]!=0):
            monedas_usadas.append(monedas[i])
            monto = monto - monedas[i]
        i-=1

    return monedas_usadas





monedas = [25, 25, 10, 1, 1, 1]
monto_a_devolver = 80

print("Usando la funcion de cambio ")
monedas_devueltas = cambio(monedas,monto_a_devolver)

print(monedas_devueltas)

