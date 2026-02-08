;16. A partir de la dirección 204 hay un conjunto de datos de longitud igual al
;dato almacenado en la dirección 203.
;Almacenar en la dirección 200 la cantidad de datos igual a cero, en la 201
;la cantidad de datos positivos y en la 202 la cantidad de datos negativos.


org 100h

    ;1-Carga de longitud en la direccion 203h
    mov ax,0006h
    mov [203h],ax
    
    ;2-Carga de datos a partir de la direccion 204h
    mov word ptr [204h],-10   
    mov word ptr [206h],0
    mov word ptr [208h],-10
    mov word ptr [20ah],-10
    mov word ptr [20ch],-10
    mov word ptr [20eh],10 
    
    ;3-limpieza de contadores e inicializacion de CX y apuntador
    
    xor dl,dl;Contador de los numero ceros
    xor dh,dh;Contador de los numeros negativos
    xor bl,bl;Contador de los numeros positivos
    
    inicio:
        mov cl,[203h];Lectura del dato en la direccion 203h
        xor ch,ch ;Dejamos en cero el registro ch
        mov di,204h;Apuntamos a la primera direccion 
        
    ;4-Logica del bucle 
    bucle:
        mov ax,[di];Lectura de la primera direccion
        add di,2;Apuntamos a la siguiente direccion
        
        cmp ax,0;La instruccion modifica ZF SF Y OF
        
        je es_cero;Si ZF=1 Entonces salta 
        jg es_positivo;Si ZF =0 y SF==OF
        jl es_negativo;SI SF<>OF
        
        es_cero:
            inc dl
            jmp siguiente
        es_positivo:
            inc dh
            jmp siguiente
        es_negativo:
            inc bl
            
        siguiente:
            loop bucle
            
            
    ;5-Cargamos los contadores en las direcciones correspondientes
    
    mov [200h],dl
    mov [201h],dh
    mov [202h],bl
                
                
ret