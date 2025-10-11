import sys

def eliminar_enemigos(enemigos, f): 
    n = len(enemigos)
    S, ultimo_ataque = eliminar_enemigos_dinamico(enemigos, f, n)
    minutos = obtener_minutos(S, ultimo_ataque, n)

    return S[n], minutos

def eliminar_enemigos_dinamico(enemigos, f, n):
    S= [0] * (n+1)
    ultimo_ataque = [0] * (n+1) # guarda el minuto del ultimo ataque para la posicion i

    for i in range(1, n+1):
        max_eliminados=0
        for k in range(i):
            enemigos_eliminados= S[k] + min(enemigos[i-1], f[i-k-1]) 
            if enemigos_eliminados > max_eliminados:
                max_eliminados = enemigos_eliminados
                ultimo_ataque[i]=k
        S[i]=max_eliminados
    return S, ultimo_ataque

def obtener_minutos(S, ultimo_ataque, n): 
    i=n
    minutos =[]
    
    while i > 0:
        minutos.append(i)
        i= ultimo_ataque[i]

    minutos.reverse() 
    return minutos


def procesar_archivo(ruta_archivo):
    enemigos = []
    f = []
    try:
        with open(ruta_archivo, 'r') as archivo:
            n =None
            contador =0
            for linea in archivo:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                
                if n is None: #primera linea
                    n = int(linea)
                    continue
                if contador <n:
                    enemigos.append(int(linea))
                else:
                    f.append(int(linea))
                
                contador+=1

            if len(enemigos) != n or len(f) != n:
                print(f"Error: el archivo {ruta_archivo} no tiene {n} valores de enemigos y {n} valores de f.")
                return None

    except FileNotFoundError:
        print(f"Error: el archivo {ruta_archivo} no existe.")
        return None
    except ValueError:
        print("Error: el archivo no tiene el formato esperado.")
        return None
    return enemigos, f

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tp2.py <archivo_entrada.txt>")
        return 1

    archivo_entrada = sys.argv[1]
    enemigos, f = procesar_archivo(archivo_entrada)

    if not enemigos or not f:
        print("No se encontraron enemigos o f válidos.")
        return 1
    
    enemigos, minutos = eliminar_enemigos(enemigos,f)

    print("Cantidad de tropas eliminadas:", enemigos)
    print("Minutos de ataque:", minutos)
    return 0

if __name__ == "__main__":
    sys.exit(main())