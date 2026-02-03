org 100h

;Vamos a configurar el modo de video  3 (texto a color, 80 columnas x 25 filas)
mov ax ,03 ; significa modo texto 80x25, 16 colores ,8 paginas ah = 0 , al = 3
int 10h ;Ejecuta!

;Cancela el destello y establece los colores   
mov ax,1003h ;al = 03 permite que el MSB controle la intensidad del color del
;caracter 
mov bx ,0;cancela el destello
int 10h

;Define el registro  de segmento en la VRAM para texto a color (b800)
mov ax, 0b800h
mov ds, ax
;Ahora vamos a imprimri 'Organizacion del computador'

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


;Vamos a colorear todos los caracteres
mov cx,11; Estamos en presencia de 11 caracteres
mov di,03h;Comienza desde el byte siguiente a 'H'

c:  mov [di],11101100b ; 1110 fondo amarillo y 1100 es el color del caracter
    add di,2
    loop c
  
  
;Esperaremos a que se oprima una tecla para que devolver el control al sistema
;Operativo 
mov ah,0
int 16h
ret
