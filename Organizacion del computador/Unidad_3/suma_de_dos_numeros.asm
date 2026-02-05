org 100h

; 1. Limpiar pantalla (Modo 3)
mov ax, 3
int 10h

; 2. Preparar ES para la pantalla (0B800h)
mov ax, 0B800h
mov es, ax

; 3. Poner datos de prueba en memoria "normal" (DS)
mov byte ptr [0200h], 5   ; Primer dato
mov byte ptr [0201h], 4   ; Segundo dato

; 4. Sumar usando un registro como intermediario
mov al, [0200h]           ; Cargamos el 5 en AL
add al, [0201h]           ; Sumamos el 4 a AL (AL ahora vale 9)
mov [0202h], al           ; Guardamos el resultado (9) en 0202h

; 5. Mostrar en pantalla
; Para ver el "9", sumamos 48 (ASCII de '0')
add al, 48                
mov ah, 0Fh               ; Color blanco sobre negro
mov es:[0], ax            ; Enviamos a la pantalla (esquina superior izquierda)

ret