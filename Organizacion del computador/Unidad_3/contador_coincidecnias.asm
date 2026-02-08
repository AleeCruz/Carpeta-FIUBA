;A partir de la dirección 204 hay un conjunto de datos de longitud igual al
;dato almacenado en la dirección 203. Almacenar en la dirección 200 la
;cantidad de datos que tienen el bit 3 en 1.
            
org 100h
   
   ;1-Carga de la longitud
   mov ax,0003h
   mov [203h],ax        
            
   ;2-Carga de daatos de 16 bits a partir de la 204h         
            
   mov [204h],1000110100001111b
   mov [206h],0001110010100101b
   mov [208h],0000000000001111b
   
   ;3-Limpieza del contador DX e inicializacion de CX y el apuntador DI
   xor dx,dx
   
   inicio:
   mov cl,[203h];Lectura de la longitud 
   xor ch,ch;Para evitar errores del bucle
   mov di,204h 
   
   
   ;4-Logica del bucle 
   
    bucle:
    mov ax,[di];Carga del registro AX con el dato apintado por [di]
    
    test ax,0008h;Op. Logico And sin afectar AX->Match ZF =0 sino ZF=1
    
    jz no_incrementar ;Revisa ZF=0 entonces no salta
    inc dx
    
    no_incrementar:
    add di,2
    loop bucle     
          
    ;5-Carga de la cantidad de datos con bit 3 en 1 en la direccion 200
    mov [200h],dx        
            
ret            
            