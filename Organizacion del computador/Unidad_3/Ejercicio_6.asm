;Vamos a imprimir 'Organizacion del computador'

;------------Instrucciones necesarias para el correcto funcionamiento--------
org 100h

;Activacion del modo de video 3
mov ax,3
int 10h;ejecuta

;Cancelacion del destello y asignacion de los colores
mov ax,1003h
mov bx,0;Cancela el destello
int 10h;Ejecuta
                 
;Asignacion de los registros para la memoria de video VRAM
mov ax,0b800h
mov ds,ax

;-----------Fin de las instrucciones para el corrcto funcionamiento-------

mov [02h],'O'
mov [04h],'r'
mov [06h],'g'
mov [08h],'a'
mov [0ah],'n'
mov [0ch],'i'
mov [0eh],'z'
mov [10h],'a'
mov [12h],'c'
mov [14h],'i'
mov [16h],'o'
mov [18h],'n'
mov [1ah],' '
mov [1ch],'d'
mov [1eh],'e'
mov [20h],'l'
mov [22h],' '
mov [24h],'C'
mov [26h],'o'
mov [28h],'m'
mov [2ah],'p'
mov [2ch],'u'
mov [2eh],'t'
mov [30h],'a'
mov [32h],'d'
mov [34h],'o'
mov [36h],'r'
mov [38h],'!'  



;Cantidad de letras y el comienzo de la salida por consola
mov cx,28
mov di,03h

;loop 
bucle:  mov [di],11101100b
        add di,2
        loop bucle

;Se debera de oprimir una tecla para asignarle el control al SO
mov ah,0
int 16h
ret