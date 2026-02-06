;Vamos a realizar el ejercicio de sumatoria e impresion de datos

.model small
.stack 100h

.data
    uni db 0
    dece db 0
    cen db 0
    datossuma db 01h,02h,03h,04h,05h,06h,07h,07h,09h,0ah

.code
    
    sumatoria proc
        mov ax,@data
        mov ds,ax
        
        xor bx,bx
        xor al,al
        mov cx,0ah
        
    acumulador: 
            add al,datossuma[bx]
            inc bx
            loop acumulador  
            
            
    inicio:
    
        ;Vamos a ingresar los datos en las variables correspondiente de data
        aam ;Dividimos AL/10 ---> AH=5 AL=4
        mov uni,al
        mov al,ah;Movimos en al el dato de ah o sea al =5
        aam; Dividimos AL/10 ---> AH=0 AL=4
        mov dece,al
        mov cen,ah
        
        ;Ahora realizamos la impresion de los datos correspondientes
        
        mov ah,02h;Funcion que permite imprimir por consola
        
        mov dl,cen
        add dl,30h
        int 21h
        
        mov dl,dece
        add dl,30h
        int 21h
        
        mov dl,uni
        add dl,30h
        int 21h
        
         
    mov ah,04ch
    int 21h
    
    sumatoria endp
    
end sumatoria
    
    
    
    