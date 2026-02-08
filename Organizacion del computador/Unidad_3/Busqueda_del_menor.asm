;17. A partir de la dirección 3002 hay un conjunto de datos de longitud dada
;en la dirección 3001. Almacenar en la dirección 3000 el dato menor.



org 100h
    
    ;1-Carga de la longitud 
    mov ax,0004h
    mov [3001h],ax
    ;2-Carga de datos a partir de las direccion 3002h
    
    mov word ptr [3002h],0050h
    mov word ptr [3004h],0010h
    mov word ptr [3006h],0025h
    mov word ptr [3008h],0060h
    
    ;3-Cargamos los contadores-pointer y elejimos el primer valor como minimo
    ;decremento de cl y apuntar al siguiente valor  
    
    mov cl,[3001h];Cargamos el registro cl con la longitud de 3001h
    xor ch,ch;Dejamos el Registro ch en cero
    mov si,3002h;El registro SI apuntara a 3002h
    
    mov ax,[si];Dejamos en AX el primer dato como si fuera minimo
    dec cl;Al tomar el primero como el menor nos queda cl-1 comparaciones
    add si,2;Apuntamos a la siguiente direccion 
    
    
    ;4-Logica del bucle para comparar los valores y actualizar el minimo 
    comparar:
        cmp [si],ax;Compara el minimo actual con el dato, altera ZF,Sf,OF 
        
        jge siguiente;Si SF<>OF no salta, en cambio, si SF==OF --> [si]<ax jmp
        
        mov ax,[si];En caso de que no salte se actualiza el nuevo menor 
        
    siguiente:
        add si,2
        loop comparar        
        
     ;5-Carga del menor dato en la direccion 3000h
     mov [3000h],ax 
    

ret 