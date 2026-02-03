;Otra vez probaremos con escribir por consola 'Ingenieria Electronia'

;--------------Instrucciones para el correcto funcionamiento---------
org 100h;Inicio del programa

;Activacion del modo de video 3
mov ax,3
int 10h

;Cancelacion del destello y asignacion de colores
mov ax,1003h
mov bx,0;Cancelacion del destello
int 10h

;Asignacion de registros de la memoria de video VRAM
mov ax,0b800h
mov ds,ax
;------------FIn de las instrucciones para el correcto funcionamiento-------

mov [02h],'I'
mov [04h],'n'
mov [06h],'g'
mov [08h],'e'
mov [0ah],'n'
mov [0ch],'i'
mov [0eh],'e'
mov [10h],'r'
mov [12h],'i'
mov [14h],'a'
mov [16h],' '
mov [18h],'E'
mov [1ah],'l'
mov [1ch],'e'
mov [1eh],'c'
mov [20h],'t'
mov [22h],'r'
mov [24h],'o'
mov [26h],'n'
mov [28h],'i'
mov [2ah],'c'
mov [2ch],'a'  


;Cantidad de letras y el comienzo de la salida 
mov cx, 22
mov di, 03h;El registro di apuntara la madireccion de video despues de 'I'

;Se realizara un respectivo loop para la asignacionde colores
estructura_de_repeticion:   mov [di],11101100b
                            add di,2
                            loop estructura_de_repeticion


























;Se debera de oprimir una tecla para el correcto funcionamiento

mov ah,0
int 16h
ret