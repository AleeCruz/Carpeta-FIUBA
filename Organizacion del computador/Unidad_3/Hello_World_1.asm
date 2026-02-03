;Vamos a realizar un programa Hello World en asm
 
;-------------Instrucciones necesarias para accdeder a la VRAM ---------
org 100h
;Vamos a activar el modo de video 3 
mov ax,3;modo de texto 80x25,16 colores,8 paginas (ah=0,al=3)
int 10h;Ejecutar 
;Cancelacion del destello y establecimiento de los colores
mov ax, 1003h;al=3 pemrite que el MSB controla la intensidad del color del char
mov bx,0;Cancela el destello
int 10h
;Define la segmentacion en la VRAM para el texto a color (B8000)
mov ax,0b800h
mov ds,ax  

;----------------------Fin de las instrucciones ----------------------

;Ejecucion del programa Hello world


mov [02h],'H'
mov [04h],'e'
mov [06h],'l'
mov [08h],'l'
mov [0ah],'o'
mov [0ch],' '
mov [0eh],'W'
mov [10h],'o'
mov [12h],'r'
mov [14h],'l'
mov [16h],'d'
mov [18h],'!'  

;Instruccion para que se lea la cantidad de letras de nuestro string
mov cx,12
mov di,03;Comenzara desde el byte despues de la letra 'H'

;----------Se realizara un loop para asignar color de fondo y letra------
c:  mov [di],11101100b ; Fondo->amarillo 1110 y letra->roja 1100
    add di,2;Busca el siguiente codigo ascii en la memoria de video VGA
    loop c ; realiza una repeticion nuevamente hasta el señalizador 'c'
   
;Mantenemos en pausa el programa hasta oprimir una tecla para devolverle 
;el control al sistema operativo
mov ah,0
int 16h
ret




