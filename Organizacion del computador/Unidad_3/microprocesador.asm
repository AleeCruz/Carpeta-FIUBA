;Escribir en la pantalla la palabra microprocesador 

;----------Instrucciones necesarias para el correcto funcionamiento--------

org 100h

;Activacion del modo de video
mov ax,3
int 10h
;Cancelacion del destello y asignacion de los colores
mov ax,1003h
mov bx,0;Cancelacion del destello
int 10h
;Asignacion de los registros de la memoria VRAM

mov ax,0b800h
mov ds,ax
;----------Fin de las instrucciones para el correcto funcionamiento------

mov [02h],'m'
mov [04h],'i'   
mov [06h],'c'   
mov [08h],'r'   
mov [0ah],'o'   
mov [0ch],'p'   
mov [0eh],'r'   
mov [10h],'o'   
mov [12h],'c'   
mov [14h],'e'   
mov [16h],'s'   
mov [18h],'a'   
mov [1ah],'d'   
mov [1ch],'o'   
mov [1eh],'r'   


;Cantidad de letras y comienzo del programa por consola
mov cx,15
mov di,03h

;bucle 
c:  mov [di],11101100b
    add di,2
    loop c


;Codigo para la inversion de las palabras      
; Supongamos que DI terminó al final de la primera palabra (en 1Eh)
; SI será nuestro "lector" que vuelve atrás
; DI será nuestro "escritor" que sigue hacia adelante             
             
             
                     
mov si, 1eh    ; Se agrega en el registro si la posicion de la ultima letra(r) 
mov di, 22h    ;Se agrega en el registro di la direccion de memoria 22h
mov cx, 15     ;Se asignara la cantidad de letras para el string

c_invertir:                                                                          
   mov ax, [si];en SI vive la direccion 1eh, en [si]=[1eh] vive r -> ax
   mov [di], ax    ;Asignamos en 'r'->[di]  o 
   ;almacenamos en [di] la letra que vive en ax o sea el caracter 'r' 
   sub si, 2       ; Se va a retroceder desde 1eh de 2 en dos en reversa
   add di, 2       ; Avanzamos desde la direccion de memoria 22h de 2 en 2
   loop c_invertir ;Realizamos el loop correspondiente 



;Se debera oprimir una tecla para el correcto funcionamiento 
mov ah,0
int 16h
ret


