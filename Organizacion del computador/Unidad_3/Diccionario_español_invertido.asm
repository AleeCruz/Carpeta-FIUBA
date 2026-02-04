;Vamos a imprimir la palabra 'Diccionario Español'
;----------------------
org 100h

mov ax,3
int 10h

mov ax,1003h
mov bx,0
int 10h

mov ax,0b800h
mov ds,ax  
;-------------------


mov [02h],'D' 
mov [04h],'i'
mov [06h],'c'
mov [08h],'c'
mov [0ah],'i'
mov [0ch],'o'
mov [0eh],'n'
mov [10h],'a'
mov [12h],'r'
mov [14h],'i'
mov [16h],'o'
mov [18h],' '
mov [1ah],'E'
mov [1ch],'s'
mov [1eh],'p'
mov [20h],'a'
mov [22h],'ñ'
mov [24h],'o'
mov [26h],'l'

;Asignacion de cantidad al string cx, e inicializacion   del apuntador di

mov cx,19
mov di,03h

;inicializacion del bucle 

repeticion: mov [di],11101100b
            add di,2
            loop repeticion
                                     
                                     
;Usaremos la logica de la inversion
;Usaremos los registro de indice para apuntar 
mov si,26h
mov di,30h
mov cx,19

inversion:  mov ax,[si]
            mov [di],ax
            sub si,2
            add di,2
            loop inversion                                     

;Oprimir una tecla para darle el control al SO
mov ah,0
int 16h
ret
