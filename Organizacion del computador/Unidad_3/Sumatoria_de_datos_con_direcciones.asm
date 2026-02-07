;Sumar el conjunto de datos de 16 bits que comienzan en la dirección 203
;y tiene una longitud dada por el dato almacenado en la dirección 202.
;Elegir los datos para que su suma sea menor a 65.536. Almacenar el
;resultado a partir de la dirección 200. 

org 100h

    ;1-Carga de registros y direcciones
    mov ax,0003h
    mov [202h],ax
    

    mov [203h],1000h
    mov [205h],2000h
    mov [207h],3000h
    
    ;Limpieza de registro del contador
    xor cx,cx

    inicio: 
    ;Lectura del registro cl de la direccion de memoria 
    mov cl,[202h]
    ;Cargamos el apuntador SI , con la direccion 203h
    mov si,203h
    ;Limpieza del registro ax,para usarlo como acumulador
    xor ax,ax
    
    suma:
        add ax,[si]
        add si,2
        loop suma
        
        
        
    ;Cargar el registro en 200 con el resultado de 16 bits
    
    mov [200h],ax
    
 

ret

