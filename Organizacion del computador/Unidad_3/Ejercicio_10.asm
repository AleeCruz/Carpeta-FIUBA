; En las direcciones 0100 y 0101 hay dos enteros positivos. Ubicar en la
;dirección 0102 el menor de los dos.

org 100h

jmp set

    set:
    ;1-Carga de datos en las direcciones 0100h y 0101h 
    
    mov al,11101111b;Se carga el valor en binario al registro al 239
    mov [0100h],al;Se carga del registro AL a la direccion 100h al 
    
    mov al,11110000b;240
    mov [0101h],al
    
    ;2-Lectura de datos de las direcciones correspondientes
    
    mov al,[0100h] ;239
    mov bl,[0101h] ;240
    
    ;3-Comparacion  y salto 
    cmp al,bl  ;Realizamos la comparacion
    
    jae AesMayor;Se realizo la comparacion al>=bl -> cf=0 salta 
    jb BesMayor;Se realizo la comparacion al<bl -> cf=1 salta
    
    
    ;Carga en la direccion de memoria 0102h
    ;dependiendo del flag cf->Salta a alguno de los 2
    AesMayor:
    mov [0102h],al
    jmp fin
    
    BesMayor:
    mov [0102h],bl
    jmp fin
    
    
    fin:
ret