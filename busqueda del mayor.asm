; En las direcciones 0100 y 0101 hay dos enteros positivos. Ubicar en la
;dirección 0102 el menor de los dos.  


org 100h
    
    ;1-Carga de datos 
    mov al,11001000b ;200
    mov [0100h],al
    
    mov al,01101011b ;107
    mov [0101h],al
    
    ;2-Lectura de datos 
    
    mov al,[0100h]
    mov bl,[0101h]
    
    cmp al,bl  ;Dado que al es mayor cf=0
    
    jae AesMayor    ;cf=0
    jb BesMayor     ;cf=1
    
    
    AesMayor:
    mov [0102h],al
    jmp fin
    
    BesMayor:
    mov [0102h],al
    jmp fin      
                
    fin:            

ret
