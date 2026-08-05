CUOTA_BASE = 5000.0  
print("=== SISTEMA DE INSCRIPCIÓN AL CLUB DEPORTIVO ===")

nombre_ingresado = input("Ingresa tu nombre completo: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros (ej. 1.75): "))

nombre_mayusculas = nombre_ingresado.upper()
cantidad_caracteres = len(nombre_ingresado)
nombre_limpio = nombre_mayusculas.replace("  ", " ") 

if edad < 13:
    categoria = "Infantil"
    precio_final = CUOTA_BASE * 0.5  
elif edad <= 17:
    categoria = "Adolescente"
    precio_final = CUOTA_BASE * 0.75 
elif edad <= 59:
    categoria = "Adulto"
    precio_final = CUOTA_BASE
else:
    categoria = "Adulto mayor"
    precio_final = CUOTA_BASE * 0.4  

print("\n" + "="*40)
print("       RESUMEN DE LA INSCRIPCIÓN       ")
print("="*40)
print(f"Nombre registrado:     {nombre_limpio}")
print(f"Largo del nombre:      {cantidad_caracteres} caracteres")
print(f"Edad:                  {edad} años")
print(f"Altura:                {altura} m")
print(f"Categoría asignada:    {categoria}")
print(f"Cuota base oficial:    ${CUOTA_BASE}")
print(f"Monto final a pagar:   ${precio_final}")
print("="*40)
print("¡Inscripción realizada con éxito!")



