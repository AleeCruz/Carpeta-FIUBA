; Sumar el conjunto de datos de 16 bits que comienzan en la dirección 203
;y tiene una longitud dada por el dato almacenado en la dirección 202.
;Elegir los datos para que su suma sea menor a 65.536. Almacenar el
;resultado a partir de la dirección 200. 



org 100h

    ;1-Carga de los datos 
    mov ax,003h
    mov [202h],ax
    
    ;2-Carga de las variables
    mov [203h],100Ah
    mov [205h],2003h
    mov [207h],0A01h
    
    ;3-Limpieza del contador e inicializacion
    xor ax,ax
    
    inicio:
        mov cl,[202h]
        xor ch,ch
        mov si,203h
    ;4-Suma en el acumulador AX    
    suma: 
        add ax,[si]
        add si,2
        loop suma
            
     ;5-Carga de datos en la direccion 200h
     mov [200h],ax
     
     
ret
    
    
