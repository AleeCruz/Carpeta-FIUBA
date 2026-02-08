;Sumar el conjunto de datos de 16 bits que comienzan en la dirección 203
;y tiene una longitud dada por el dato almacenado en la dirección 202.
;Elegir los datos para que su suma sea menor a 65.536. Almacenar el
;resultado a partir de la dirección 200.  

org 100h

;1-Carga de datos para la suma y longitud 

    mov ax,03h
    mov [202h],ax
    
    mov [203h],1000h
    mov [205h],2000h
    mov [207h],3000h
    
    
    ;Limpieza del registro 
    xor cx,cx
    
    inicio:
    
        mov cl,[202h];Lectura de la cantidad de datos almacenados en 202
        xor ax,ax;dejamos el acumulador vacio para la suma
        mov si,203h;Direccionamos el registro SI para apuntarlo
    
    ;Logica de la suma para cumularlo en AX    
    suma:
        add ax,[si]
        add si,2
        loop suma 
        
    ;Carga del total en la direccion 200 que es un dato de 16 bits
    mov [200h],ax    


ret 