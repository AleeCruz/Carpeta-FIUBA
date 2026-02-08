;17. A partir de la dirección 3002 hay un conjunto de datos de longitud dada
;en la dirección 3001. Almacenar en la dirección 3000 el dato menor.




org 100h
set:
    ; 1. Inicializamos la longitud en 3001h
    mov byte ptr [3001h], 4    ; Vamos a probar con 4 datos
    ; 2. Cargamos los datos (16 bits cada uno) a partir de 3002h
    mov word ptr [3002h], 0050h ; 80 decimal
    mov word ptr [3004h], 0010h ; 16 decimal (este será el menor)
    mov word ptr [3006h], 0025h ; 37 decimal
    mov word ptr [3008h], 0060h ; 96 decimal
jmp inicio
inicio:
    mov cl, [3001h]     ; Cargamos la longitud en CL
    xor ch, ch          ; Limpiamos CH para que CX sea exacto
    mov si, 3002h       ; SI apunta al primer dato
    
    ; PASO CLAVE: Tomamos el primer dato como el "menor provisional"
    mov ax, [si]        
    dec cx              ; Como ya tomamos el primero, nos quedan CX-1 comparaciones
    add si, 2           ; Movemos el puntero al segundo dato
comparar:
    cmp [si], ax        ; modifica ZF,SF y OF.
    jge siguiente       ; si SF==OF entonces salta, caso contrario continua    
    ; Si llegamos aquí, encontramos un nuevo menor
    mov ax, [si]        ; Actualizamos AX con el nuevo valor mínimo
siguiente:
    add si, 2           ; Apuntamos al siguiente dato
    loop comparar       ; Repetimos hasta revisar toda la lista
    ; 3. Almacenamos el resultado final (el menor) en 3000h
    mov [3000h], ax
ret