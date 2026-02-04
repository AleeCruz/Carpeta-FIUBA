;El ejercicio es simple debemos de escribir Alexander y escribirlo al reves

;-----------Instrucciones necesarias para el correcto funcionamiento 

org 100h
;activacion del modo de video 
mov ax,3
int 10h
;Cancelacion y asignacion de los colores 
mov ax,1003h ;ah=03 se encarga deL MSB para el correcto uso de colores
mov bx,0; Cancelacion del destello   
int 10h
;Asignacion de registros de la memoria VRAM
mov ax,0b800h
mov ds,ax
;-----------Fin de las instrucciones para el correcto funcionamiento 


mov [02h],'A'
mov [04h],'l'
mov [06h],'e'
mov [08h],'x'
mov [0ah],'a'
mov [0ch],'n'
mov [0eh],'d'
mov [10h],'e'
mov [12h],'r'


;Asignar el tamaño del string y usar un registro de indices DI
mov cx,9
mov di,03h

;Bucle

c:  mov [di],11101100b
    add di,2
    loop c
    
;Vamos a invertir las palabras 

;Asignacion hacia 2 registros SI para ir en revera y
;DI para apuntar a una nueva direccion en la cual comenzara
;Asignacion de la cantidad de letras al registro cx

mov si,12h
mov di,16h }
mov cx,9

invertir: 
    mov ax,[si];EL contenido que vive en 12h osea 'r' = [si] se asigna a ax
    mov [di],ax; Se le asignara el dato almacenado en ax a las direccion 16h
    sub si,2; Se le quitara de 2 en 2 desde 12h para la reversa
    add di,2; Se le agregara de 2 en 2 desde 16h
    loop invertir





















;Se debera oprimir una tecla para devolver el control al SO
mov ah,0
int 16h
ret
