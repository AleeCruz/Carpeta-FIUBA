;Vamos a realizar el ejercicio numero 8 de la guia de ejercicios
.model small
.stack 100h
.DATA
    cen db 0
    dece db 0
    uni db 0
    
    DATOSSUM db 01h,02h,03h,04h,05h ;Son datos que 
             db 06h,07h,08h,09h,0Ah ;vamos a procesar
         
.CODE
SUMA PROC
    MOV AX,@DATA
    mov DS,AX
    XOR BX,BX  ;indice de acceso al area de datos
    XOR DL,DL  ;acumulador de datos 
    MOV CX,0Ah ;numero de datos a procesar 
    
    
ACUMULA: 
    ADD DL,DATOSSUM[BX]
    INC BX
    loop ACUMULA
        
        
inicio:    
    mov al,DL;Asigno el valor de la suma en decimal al registro AL
    aam      ;ajuste el valor en AL  por: AH los digitos mas significativos
    
    mov uni,al
    mov al,ah
    
    aam
    mov cen,ah
    mov dece,al
    
    mov ah,02h 
    
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
end
    
    