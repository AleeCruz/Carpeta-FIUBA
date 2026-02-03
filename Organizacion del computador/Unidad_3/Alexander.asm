;vamos a imprimir por pantalla nuestro nombre de fondo amarillo y color rojo

;---------------Instrucciones para que el programa fucnione-------------
org 100h

;activa el modo de video 3
mov ax,3
int 10h

;Cancelacion del destello y eztablecimiento de los colores
mov ax,1003h;al=03 permite que el MSB  controle la intensidad del color del char
mov bx,0  
int 10h

;Definir los registros del segmento de en la VRAM para el texto a color(B800)
mov ax,0b800h
mov ds,ax

;---------------Fin de las instrucciones necesarias para que funcione---------

;Aca es donde comienza el programa

mov [02h],'A' 
mov [04h],'l'
mov [06h],'e'
mov [08h],'x'
mov [0ah],'a'
mov [0ch],'n'
mov [0eh],'d'
mov [10h],'e'
mov [12h],'r'
mov [14h],'!'    


;Cantidad de letras a imprimir y desde que lugar comenzara a imprimir
mov cx,10
mov di,03


bucle:  mov [di],11101100b;Fondo-amarillo y Letra-Roja
        add di,2
        loop bucle
        
        
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
;Dejar que se oprima una tecla para darle el control al SO
mov ah,0
int 16h
ret
