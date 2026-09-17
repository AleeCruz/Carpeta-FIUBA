def suma_anteriores(arreglo,n):

    for(i=0;i<n;i++):
        suma_anteriores=0
        for (j=0;j<i;j++):
            suma_anteriores += arreglo[j]
        
        arreglo[i] -= suma_anteriores