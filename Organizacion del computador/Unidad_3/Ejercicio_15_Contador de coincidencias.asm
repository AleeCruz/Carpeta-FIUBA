;A partir de la dirección 204 hay un conjunto de datos de longitud igual al
;dato almacenado en la dirección 203. Almacenar en la dirección 200 la
;cantidad de datos que tienen el bit 3 en 1.


org 100h

    ; 1. Longitud en 203h (solo 1 byte para no pisar la 204h)
    mov [203h], 0004h
    
    ; 2. Carga de datos de 16 bits (cada uno ocupa 2 bytes)
    mov [204h], 1000110100001111b ; Dato 1 (Bit 3 es 1)
    mov [206h], 0001110010100101b ; Dato 2 (Bit 3 es 0)
    mov [208h], 0000000000001111b ; Dato 3 (Bit 3 es 1)
    mov [20ah], 0000010000001111b 
    ;3-Limpieza del contador match DX e inicializacion de CX y puntero
    xor dx, dx 

    inicio:
        mov cl, [203h]
        xor ch, ch ; Aseguramos CX para el loop
        mov di, 204h


;4-Logica del Bucle
bucle:
    mov ax, [di];Carga del dato apuntado en AX

;Logica del AND sin alterar el registro AX and 08h verifica la coincidencia
    test ax, 0008h;Si hay coincidencias ZF=0 caso contrario ZF=1
                           
    jz no_incrementar;jz no salta  si ZF=0 caso contrario salta si ZF=1
    inc dx;como no salta el contador dx aumenta en 1 por la coincidencia 

no_incrementar:
    add di, 2 ;Apuntamos a la siguiente direccion 
    loop bucle;Repetimos el bucle hasta terminar CX en cero


;5-Carga de coincidencias en la direccion 200h
    mov [200h], dl

ret