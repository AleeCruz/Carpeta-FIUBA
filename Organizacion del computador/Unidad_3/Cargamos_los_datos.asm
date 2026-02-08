;A partir de la dirección 204 hay un conjunto de datos de longitud igual al
;dato almacenado en la dirección 203. Almacenar en la dirección 200 la
;cantidad de datos que tienen el bit 3 en 1.           


org 100h
    
    ;1-Carga de la longitud 
    mov ax,0005h
    mov [203h],ax
    
    ;2-Carga de datos en las direcciones a parti de la 204h
    mov [204h],1000110100001111b 
    mov [206h],0001110010100101b 
    mov [208h],0000000000001111b
    mov [20ah],1000110100001111b
    mov [20ch],1000110100001111b 
    
    
    ;3-Limpieza del contador e inicializacion del CX y el apuntador
    
    xor dx,dx
    inicio: 
        mov cx,[203h]
        xor ch,ch
        mov di,204h
        
    ;4-Logica del bucle 
    bucle:
    mov AX,[di];Cargamos el registro con el primer valor 
    
    test AX,0008h;Realizamos AX and 08h si hay match ZF=0 caso contrario ZF=1
    
    jz no_incrementar;SI ZF=0 no salta caso contrario si ZF=1 salta
    inc dx;Aumentamos en uno el acumulador
    
    no_incrementar:
    add di,2;Avanza a la siguiente direccion
    loop bucle
    
    ;5-Cargamos la cantidad de coincidencias en la direccion 200h
    mov [200h],dx
    
ret






