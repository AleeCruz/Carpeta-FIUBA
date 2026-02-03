;Realizaremos un adios mundo 

;-------Instrucciones necesarias para que funciones correctamente----------

org 100h 

mov ax,3
int 10h  

mov ax,1003h
mov bx,0
int 10h

mov ax,0b800h
mov ds,ax

;--------------Fin de las instrucciones-----------------     
;A partir de aqui se ingresaran los caracteres y el respectivo loop


mov [02h],'A'
mov [04h],'d' 
mov [06h],'i'
mov [08h],'o'
mov [0ah],'s'
mov [0ch],' '
mov [0eh],'M'
mov [10h],'u'
mov [12h],'n'
mov [14h],'d'
mov [16h],'o'
mov [18h],'!'
mov [1ah],'!'  

;Pondremos la cantidad de letras y desde donde se van a imprimir 
mov cx,13
mov di,03    

;Ahora agregaremos el color a cada fondo-caracter y su respectivo loop

bander: mov [di],11101100b
        add di,2
        loop bander






           
           
           
           
           
           



;Se Espera a que se oprima una tecla para darle el control al SO
               
mov ah,0
int 16h
ret