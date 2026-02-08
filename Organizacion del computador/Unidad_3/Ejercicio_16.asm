;16. A partir de la dirección 204 hay un conjunto de datos de longitud igual al
;dato almacenado en la dirección 203.
;Almacenar en la dirección 200 la cantidad de datos igual a cero, en la 201
;la cantidad de datos positivos y en la 202 la cantidad de datos negativos.


org 100h
    
    ;1-Carga de la longitud en la direccion 203h
    
    mov byte ptr [203h], 6     ; Longitud (1 byte)
    
    ;2-Carga de datos positivos, negativos y ceros en las direcciones 
    mov word ptr [204h], -24    ; Negativo
    mov word ptr [206h], 0      ; Cero
    mov word ptr [208h], 5      ; Positivo  
    mov word ptr [20ah], 0      ; Cero
    mov word ptr [20ch], -2     ; Negativo
    mov word ptr [20eh], 0      ; Cero

    ;3-Limpieza de registros de conteo e inicializacion de CX y apuntadores
    xor dx, dx  ; DL = Ceros, DH = Negativos
    xor bx, bx  ; BL = Positivos
    jmp inicio

    inicio:
        mov cl, [203h]
        xor ch, ch
        mov di, 204h
    
    
    
    ;4-Logica del bucle
    repetir:
        mov ax, [di];Cargamos AX con el dato de la primera direccion
        add di, 2 ; Avanzamos de a 2 bytes (16 bits)
        
        cmp ax, 0 ;Realiza una comparacion si ambos son iguales ZF=0
        je es_cero ;Si ZF=0 no salta, caso contrario si ZF=1 salta
        jl es_menor
        jg es_mayor
    
    es_cero:
        inc dl
        jmp siguiente
    
    es_menor:
        inc dh
        jmp siguiente
    
    es_mayor:
        inc bl
    
    siguiente:
        loop repetir
    
    
    
    ;5- Cargamos los datos en las direcciones correspondientes
    mov [200h], dl    ; Ceros
    mov [201h], bl    ; Positivos
    mov [202h], dh    ; Negativos

ret













