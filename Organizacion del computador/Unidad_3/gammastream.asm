;Se imprimira GammaStream en la memoria de video 

;----------Instrucciones necesarias para que el programa funcione------

org 100h;Comienzo del programa

;Inicio del modo de video 3
mov ax,3
int 10h

;Cancelacion del destello y establecimiento de los colores
mov ax, 1003h; al = 03 permite que el MSB controle la intensidad del color char
mov bx,0 ;cancela el destello
int 10h

;Definicion de los registron del segmento en la VRAM para texto a color(B800)
mov ax,0b800h
mov ds,ax

;-------------Fin de las instrucciones para el correcto funcionamiento-------


mov [02h],'G'
mov [04h],'a'
mov [06h],'m'
mov [08h],'m'
mov [0ah],'a'
mov [0ch],' '
mov [0eh],'S'
mov [10h],'t'
mov [12h],'r'
mov [14h],'e'
mov [16h],'a'
mov [18h],'m'
mov [1ah],'!'
    
;Asignaremos la cantidad de letras y el comienzo despues de la letra 
mov cx,13
mov di,03h   

;Ahora viene el bucle para la asignancion de propiedades de cada letra
bucle:  mov [di],11101100b
        add di,2
        loop bucle
        
        

















;Se debera de oprimir una tecla para asignarle el control al SO
mov ah,0
int 16h
ret

