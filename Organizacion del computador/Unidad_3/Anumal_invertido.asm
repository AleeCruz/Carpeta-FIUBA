;Vamos a imprimir por consola 'Animal'

org 100h

mov ax,3
int 10h

mov ax,1003h
mov bx,0
int 10h

mov ax,0b800h
mov ds,ax


mov [02h],'A'
mov [04h],'n'
mov [06h],'i'
mov [08h],'m'
mov [0ah],'a'
mov [0ch],'l'
mov [0eh],'!'   

;Definimos la cantidad y el inicio del programa con el apuntador
mov cx,7
mov di,03h

;Bucle
repeticion: mov [di],11101100b
            add di,2
            loop repeticion
            

;Codigo para la inversion de la palabra
;Asignacion de direcciones a los apntadores y contador

mov si,0eh;Apunta siempre a la direccion de la ultima letra
mov di,12h;Deja un espacio en blanco para que no se superponga
mov cx,9;Asignaremos la cantidad de letras del string

inversion:  mov ax,[si]
            mov [di],ax
            sub si,2
            add di,2
            loop inversion



















mov ah,0
int 16h
ret
