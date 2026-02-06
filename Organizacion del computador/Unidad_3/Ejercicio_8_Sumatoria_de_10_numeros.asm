.model small ; directivas que permiten dar un modelo pequeño
.stack ;Reserva un segmento de memoria en el stack por lo general es de 64K


.data
    cen db 0
    dece db 0
    uni db 0
    ; La suma de 1 a 10 es 55 (37h en hexadecimal)
    datossum db 01h,02h,03h,04h,05h,06h,07h,08h,09h,0ah

.code 



    ;Todo este codigo sirve para organizar el codigo
    
    suma proc;Esto es el (procedure) abre la funcion 
        
        mov ax,@data
        mov ds,ax
        
        xor bx,bx
        xor al,al      ; Usamos AL para la suma total
        mov cx,0ah     ; 10 elementos
    
    acumula: 
            add al, datossum[bx] ; SUMAMOS, no movemos
            inc bx
            loop acumula 
            
    inicio:
            ; AL ahora tiene 55
            aam              ; Divide AL por 10. AH = Cociente (5), AL = Residuo (5)
            mov uni,al       ; Guardamos unidades (5)
            mov al,ah        ; Pasamos el 5 a AL
            aam              ; Volvemos a dividir para sacar centenas
            
            mov cen,ah       ; Centenas (0)
            mov dece,al      ; Decenas (5)
            
            ; --- IMPRESIÓN ---
            mov ah,02h       ; Función para imprimir carácter
            
            mov dl,cen
            add dl,30h       ; Convertir a código ASCII
            int 21h
            
            mov dl,dece
            add dl,30h
            int 21h
            
            mov dl,uni
            add dl,30h
            int 21h
                      
            mov ah,4ch       ; Salir del programa
            int 21h
    suma endp;Esto es el end procedure de suma 
             ;O sea es el fin del bloque de codigo de la funcion llamada
    
    
    
    
    
end suma;1-Indica el final fisico del archivo
        ;2-Define el "Punto de entrada" (Entry point)
        ;Cuando se escribe el nombre de tu procedimiento al lado de end 
        ;Se le esta diciendo que Cuando cargues este programa desde 
        ;Memoria, empeza a ejecutar desde la etiqueta de suma.