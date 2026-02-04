;Escribir Chainsawman por consola
;----------Instrucciones necesarias para el correcto funcionamiento--------

org 100h; Inicio del programa
;Activacion del modo de video 3
mov ax,3
int 10h
;Cancelacion del destello y asignacion de colore
mov ax,1003h
mov bx,0
int 10h
;Asignacion de registro de la VRAM
mov ax,0b800h
mov ds,ax

;------------------Fin de las instrucciones----------------------


mov [02h],'C'
mov [04h],'h'
mov [06h],'a'
mov [08h],'i'
mov [0ah],'n'
mov [0ch],'s'
mov [0eh],'a'
mov [10h],'w'
mov [12h],'M'
mov [14h],'a'
mov [16h],'n'  

;Cantidad de letras e inicializacion de el registro de indices
mov cx,11
mov di,03h

bucle:  mov [di],11101100b;Asignacion de los colores a cada letras y fondo
        add di,2
        loop bucle



;--------Oprimir una tecla para dejar el contrl al SO
mov ah,0
int 16h
ret