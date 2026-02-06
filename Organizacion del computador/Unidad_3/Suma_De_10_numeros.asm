

.MODEL SMALL
.STACK 100h



.DATA
    cen  db 0
    dece db 0
    uni  db 0
    DATOSSUM db 01h,02h,03h,04h,05h,06h,07h,08h,09h,0Ah 
  
  
  
  
  
.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    XOR BX, BX  ; Ponemos BX en 0 (será nuestro índice: 0, 1, 2...)
    XOR DL, DL  ; Ponemos DL en 0 (será nuestra "bolsa" donde acumulamos suma)
    MOV CX, 0Ah ; Cantidad de datos

ACUMULA: 
    ADD DL, DATOSSUM[BX]
    INC BX
    LOOP ACUMULA

    ; --- Separación de dígitos ---
    MOV AL, DL    ; AL = 55 (37h)
    MOV AH, 0     ; Limpiamos AH por seguridad antes de AAM
    AAM           ; AL = 5 (uni), AH = 5 (dece)
    MOV uni, AL
    
    MOV AL, AH    ; Movemos las decenas a AL para procesar centenas
    AAM           ; AH = 0 (cen), AL = 5 (dece)
    MOV cen, AH
    MOV dece, AL





    ; --- Mostrar en pantalla ---
    MOV AH, 02h 
    
    ; Imprimir Centenas
    MOV DL, cen
    ADD DL, 30h
    INT 21h
    
    ; Imprimir Decenas
    MOV DL, dece
    ADD DL, 30h
    INT 21h
    
    ; Imprimir Unidades
    MOV DL, uni
    ADD DL, 30h
    INT 21h
    
    ; Salida al DOS
    MOV AX, 4C00h
    INT 21h 
    
    
MAIN ENDP
END MAIN