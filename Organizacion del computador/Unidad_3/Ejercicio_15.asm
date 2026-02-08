;A partir de la dirección 204 hay un conjunto de datos de longitud igual al
;dato almacenado en la dirección 203. Almacenar en la dirección 200 la
;cantidad de datos que tienen el bit 3 en 1.           


org 100h

set:
    ; 1. Cargamos un valor en la direccion 203h
    mov bx,0003h
    mov [203h],bx
    
    ; 2. Carga de datos de 16 bits en las direcciones a partir de la 204h 
    mov [204h], 1000110100001111b ; Dato 1 (Bit 3 es 1)
    mov [206h], 0001110010100101b ; Dato 2 (Bit 3 es 0)
    mov [208h], 0000000000001111b ; Dato 3 (Bit 3 es 1)

    xor dx, dx ;Dejamos en cero a dx

inicio:
    mov cl,[203h] ;Lectura de la longitud de la direccion 203h
    xor ch,ch ;Aseguramos que ch no tenga valores extras para el loop
    mov di,204h ;Apuntamos con el Resgistro de indice a la dir 204h

repetir:
    mov ax, [di];Cargamos el registro AX desde la direccion de memoria 
    
    ; Usamos TEST en lugar de AND para no destruir el valor de AX
    ; El bit 3 corresponde al valor hexadecimal 08h
    test ax, 0008h  
    
    jz no_incrementar ; Si el bit es 0, saltamos el incremento
    inc dx            ; Si el bit es 1, incrementamos nuestro contador

    no_incrementar:
        add di, 2         ; Pasamos al siguiente dato (16 bits = 2 bytes)
        loop repetir      ; El loop DEBE estar aquí para que siempre se ejecute

    ; 3. Guardamos el resultado final en 200h
    mov [200h], dl

ret