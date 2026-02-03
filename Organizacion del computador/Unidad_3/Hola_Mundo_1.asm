
;Estas son la directivas que siempre deben de estar presente
;--------------------------------
org 100h

;Vamos a activar el modo de video
mov ax,3 ;modo de texto 80x25,16 colores,8 paginas (ah=0,al=3)
int 10h

;Cancela el destello y establece los colores
mov ax ,1003h;al =03 permite que el MSBcontrole la intensidad del color del char
mov bx,0;cancela el destello
int 10h

;Define los registros del segmento en la VRAM para texto a color(B8000)  
mov ax,0b800h
mov ds,ax

;--------------------FIn de las directivas------------------

;-------------------Ahora podremos imprimir Hola Mundo --------------------
;Asignaremos una letra a cada seccion de la memoria VRAM
mov [02h],'H'   
mov [04h],'o'
mov [06h],'l'
mov [08h],'a'
mov [0ah],' '
mov [0ch],'M'
mov [0eh],'u'
mov [10h],'n'
mov [12h],'d'
mov [14h],'o'
mov [16h],'!'   

;Pondremos la cantidad de letras que se van a imprimir
mov cx,11;numero de caracteres que tendra la cadena de texto
mov di,03h; comenzara desde el byte despues de de 'H'

         ;Ahora realizaremos un bucle hasta qe 
c:  mov [di],11101100b ;Se le asigno el color fondo-amarillo letra-roja
    add di,2;Busca el siguiente codigo ascii en la memoria de video Vga
    loop c
;Espera a que se oprima una tecla para devolver el control al sistema
;Operativo
mov ah, 0
int 16h   
ret