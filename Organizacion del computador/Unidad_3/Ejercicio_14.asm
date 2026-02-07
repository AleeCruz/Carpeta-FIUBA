;14. Sumar el conjunto de datos de 16 bits que comienzan en la dirección 203
;y tiene una longitud dada por el dato almacenado en la dirección 202.
;Elegir los datos para que su suma sea menor a 65.536. Almacenar el
;resultado a partir de la dirección 200.


org 100h

set:
    ; 1. Cantidad de datos: Usamos solo 1 byte en 202h para no pisar la 203h
    mov  ax,03h
    mov  [202h],ax ;La direccion de memoria 202 ya esta cargada con 3

    ; 2. Carga de datos: Usamos 'word ptr' para cargar 16 bits correctamente
    ; El 8086 guardará automáticamente el byte bajo en la dir menor y el alto en la mayor
    mov [203h], 8D0Fh  ; 36111d  ah=8D y al=0F
    mov [205h], 1CA5h  ; 7333d
    mov [207h], 000Fh  ; 15d

    ;Limpieza de registros 
    xor ax,ax
    xor cx, cx

jmp inicio

inicio:
    mov cl, [202h]      ; Cargamos la cantidad de datos (3)
    mov si, 203h        ; SI apunta al primer dato (203h)
    xor ax, ax          ; AX será nuestro acumulador (empezamos en 0)
    

suma:
    add ax, [si]        ; Suma el contenido de 16 bits en la dirección SI a AX
    add si, 2           ; Saltamos 2 bytes para ir al siguiente dato de 16 bits
    loop suma           ; Repite hasta que CX sea 0

    ; 3. Almacenamos el resultado en 200h y 201h
    ; Al guardar AX, el procesador pone AL en 200h y AH en 201h
    mov [200h], ax

ret
