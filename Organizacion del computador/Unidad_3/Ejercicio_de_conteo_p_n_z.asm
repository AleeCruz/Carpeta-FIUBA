;16. A partir de la dirección 204 hay un conjunto de datos de longitud igual al
;dato almacenado en la dirección 203.
;Almacenar en la dirección 200 la cantidad de datos igual a cero, en la 201
;la cantidad de datos positivos y en la 202 la cantidad de datos negativos.


org 100h  

    ;1-Carga de la longitud en la direccion 203h
    mov ax,0006h
    mov [203h],ax 
    
    ;2-Carga de datos a partir de las direcciones 204h en adelante 
    mov word ptr [204h],100
    mov word ptr [206h],200
    mov word ptr [208h],300
    mov word ptr [20ah],0
    mov word ptr [20ch],-1
    mov word ptr [20eh],0 
    
    ;3-Limpieza de registro e inicializacion de CX y el punteros
    xor dl,dl;Contador para los cero
    xor dh,dh;Contador para los negativos
    xor bl,bl;contador para los positivos
    inicio:
    mov cl,[203h];Leectura de la longitud en cl
    xor ch,ch;Evitamos que cx no tenga vueltas extras
    mov di,204h;Apuntamos con di a la direccion 204h
    
    ;4-Bucle
    bucle:
        mov ax,[di];Cargamos el Registro AX con el dato de [di] apuntado
        add di,2 ;Apuntamos al siguiente valor
        
        cmp ax,0; Modifica el Flag ZF , SF y OF dependiendo del caso
        
        je es_cero;En caso de que ZF =1 Salta automaticamente
        jg es_positivo;En caso de que ZF=0 y SF==OF salta 
        jl es_negativo;En caso de que SF <> OF entonces salta 

        es_cero:
            inc dl
            jmp siguiente
        
        es_positivo:
            inc bl
            jmp siguiente
        
        es_negativo:
            inc dh
            
        siguiente:
            loop bucle
            
    ;5-Carga de datos en las direcciones correspondientes
    
    mov [200h],dl
    mov [201h],bl
    mov [202h],dh
     

    

ret
