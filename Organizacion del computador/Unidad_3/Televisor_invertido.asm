;Realizar un programa que imprima por pantalla 'Televisor'

org 100h

mov ax,3
int 10h  

mov ax,1003h
mov bx,0
int 10h

mov ax,0b800h
mov ds,ax

;Instrucciones para imprimir por consola

;Se agregaron datos a las direcciones de memoria correspondientes
mov [02h],'T'
mov [04h],'e'
mov [06h],'l'
mov [08h],'e'
mov [0ah],'v'
mov [0ch],'i'
mov [0eh],'s'
mov [10h],'o'
mov [12h],'r'

;Contador de letras y desde donde apuntara di
mov cx,9
mov di,03h

;Bucle para la impresion de los datos por consola 
bucle_de_impresion: mov [di],11101100b
                    add di,2
                    loop bucle_de_impresion
                    
                    
                    
;Vamos a imprimir al reves las letras 

mov si,12h
mov di,16h
mov cx,9

inversion:  mov ax,[si]
            mov [di],ax
            sub si,2
            add di,2
            loop inversion















mov ah,0
int 16h
ret