;Un byte se encuentra en la dirección 0100. Ubicar en la dirección
;0101 su nible más significativo.  

org 100h

;1 cargamos en la direccion de memoria 100 un numero aleatorio
mov al,11001101b
mov [100h],al

;2 Leemos de la direccion de memoria 101 el dato cargado
mov al,[100h]
;3 Realizamos una mascara and para obtener el nible mas significativo
and al,11110000b
;4 Almacenamos en la direccion de memoria 101 el dato modificado
;con el nible mas significativo
mov [101h],al
ret





