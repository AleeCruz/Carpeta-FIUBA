import numpy as np
import matplotlib.pyplot as plt

# --- 1. DATOS INICIALES (Jugo de Pomelo) ---
altura_experimento = np.array([
    10.249, 9.745, 8.893, 8.299, 7.632, 6.812, 6.151, 5.711,
    5.078, 4.415, 3.911, 3.376, 3.128, 2.775, 2.366, 1.987,
    1.514, 1.262, 1.136, 0.788, 0.600, 0.537, 0.441, 0.315,
    0.161
])
#--Son los datos de entrada que corresponden a la alturas correspondientes que fuimo analizando 
#COn el imageJ----

tiempo_experimento = np.array([
    0, 0.83, 1.67, 2.5, 3.33, 4.13, 5.00, 5.83, 6.67, 7.50,
    8.60, 9.17, 10.0, 10.83, 11.67, 12.5, 13.33, 14.17,
    15.0, 15.83, 16.67, 17.5, 18.33, 19.17, 20.0
])

#Tenemos entonce el conjunto de datos del tiempo  que fueron medidas desde el timepo inicial 
#En la c


valores_totales = np.arange(0, 25)#Cantidad de datos totales que vamos ausar osea las 
#Las muestras de alturas que hemo seleccionado




#Lo unico que se realiza en esta parte del codigo es que se normalice la altura de nuestras mediciones
# la normalizacion la obtuvimos con diviv
#

# Normalizamos la altura
altura_0 = altura_experimento[0]
altura_normalizada = altura_experimento / altura_0








#Esta seccion de codigo lo unico que hace es el filtro correspondiente
#Para valores con un error realitivo mayor al 10 de la altura.
#Descartamos medicioes 


# --- 2. FILTRO DEL 10% ---
# ¡Solo usamos los datos buenos para CREAR los modelos!
mascara = altura_experimento > 0.5             
mejor_tiempo = tiempo_experimento[mascara]
mejor_altura = altura_normalizada[mascara]
mejores_valores = len(mejor_tiempo)

# --- 3. FUNCIONES BASE ---
fila0 = np.ones(mejores_valores)
fila1 = mejor_tiempo
fila2 = mejor_tiempo**2
fila3 = mejor_tiempo**3

print("--- COEFICIENTES OBTENIDOS POR MÉTODO MATRICIAL ---")

# ==========================================
# MODELO CUADRÁTICO
# ==========================================
matriz_cuadratica = np.array([
    [np.inner(fila0, fila0), np.inner(fila0, fila1), np.inner(fila0, fila2)],
    [np.inner(fila1, fila0), np.inner(fila1, fila1), np.inner(fila1, fila2)],
    [np.inner(fila2, fila0), np.inner(fila2, fila1), np.inner(fila2, fila2)]
])

vector_dependiente = np.array([
    np.inner(fila0, mejor_altura),
    np.inner(fila1, mejor_altura),
    np.inner(fila2, mejor_altura)
])

# Resolvemos M * c = b
coeficientes_cuadraticos = np.linalg.inv(matriz_cuadratica) @ vector_dependiente
coeficiente_cuadratico_a = coeficientes_cuadraticos[0]
coeficiente_cuadratico_b = coeficientes_cuadraticos[1]
coeficiente_cuadratico_c = coeficientes_cuadraticos[2]

print(f"\nCuadrático: a={coeficiente_cuadratico_a:.4f}, b={coeficiente_cuadratico_b:.4f}, c={coeficiente_cuadratico_c:.4f}")

# Evaluación en tiempo experimental completo para el ECM (Error Cuadrático Medio)
y_fit_cuad = coeficiente_cuadratico_a + coeficiente_cuadratico_b * tiempo_experimento + coeficiente_cuadratico_c * (tiempo_experimento**2)

# ==========================================
# MODELO CÚBICO
# ==========================================
matriz_cubica = np.array([
    [np.inner(fila0, fila0), np.inner(fila0, fila1), np.inner(fila0, fila2), np.inner(fila0, fila3)],
    [np.inner(fila1, fila0), np.inner(fila1, fila1), np.inner(fila1, fila2), np.inner(fila1, fila3)],
    [np.inner(fila2, fila0), np.inner(fila2, fila1), np.inner(fila2, fila2), np.inner(fila2, fila3)],
    [np.inner(fila3, fila0), np.inner(fila3, fila1), np.inner(fila3, fila2), np.inner(fila3, fila3)]
])

# Vector dependiente para el modelo cúbico
vector_dependiente_cubico = np.array([
    np.inner(fila0, mejor_altura),
    np.inner(fila1, mejor_altura),
    np.inner(fila2, mejor_altura),
    np.inner(fila3, mejor_altura)
])

# Resolvemos M * c = b para el modelo cúbico
vector_coeficientes_cubicos = np.linalg.inv(matriz_cubica) @ vector_dependiente_cubico

coeficiente_cubico_a = vector_coeficientes_cubicos[0]
coeficiente_cubico_b = vector_coeficientes_cubicos[1]
coeficiente_cubico_c = vector_coeficientes_cubicos[2]
coeficiente_cubico_d = vector_coeficientes_cubicos[3]

print(f"Cúbico: a={coeficiente_cubico_a:.4f}, b={coeficiente_cubico_b:.4f}, c={coeficiente_cubico_c:.4f}, d={coeficiente_cubico_d:.4f}")

# Evaluación en tiempo experimental completo para el ECM (Error Cuadrático Medio)
y_fit_cub = coeficiente_cubico_a + coeficiente_cubico_b * tiempo_experimento + coeficiente_cubico_c * (tiempo_experimento**2) + coeficiente_cubico_d * (tiempo_experimento**3)

# ==========================================
# MODELO EXPONENCIAL (Linealizado)
# ==========================================
Y_ln = np.log(mejor_altura) # Transformación para linealizar

matriz_exponencial = np.array([
    [np.inner(fila0, fila0), np.inner(fila0, fila1)],
    [np.inner(fila1, fila0), np.inner(fila1, fila1)]
])

# Vector dependiente para el modelo exponencial
vector_dependiente_exponencial = np.array([
    np.inner(fila0, Y_ln),
    np.inner(fila1, Y_ln)
]).reshape(2,1)

# Resolvemos M * c = b para el modelo exponencial
vector_coeficientes_exponenciales = np.linalg.inv(matriz_exponencial) @ vector_dependiente_exponencial

coeficiente_exponencial_a = vector_coeficientes_exponenciales[0, 0]
coeficiente_exponencial_b = vector_coeficientes_exponenciales[1, 0]

print(f"Exponencial: a={coeficiente_exponencial_a:.4f}, b={coeficiente_exponencial_b:.4f}")

# Evaluación en tiempo experimental completo para el ECM (Error Cuadrático Medio)
Y_fit_exp = coeficiente_exponencial_a + coeficiente_exponencial_b * tiempo_experimento
y_fit_exp = np.exp(Y_fit_exp) # Volvemos al espacio original

# --- 4. CÁLCULO DEL ERROR CUADRÁTICO MEDIO (ECM) ---
# Se calcula usando TODOS los datos experimentales
ecm_cuad = np.inner(altura_normalizada - y_fit_cuad, altura_normalizada - y_fit_cuad) / len(tiempo_experimento)
ecm_cub = np.inner(altura_normalizada - y_fit_cub, altura_normalizada - y_fit_cub) / len(tiempo_experimento)
ecm_exp = np.inner(altura_normalizada - y_fit_exp, altura_normalizada - y_fit_exp) / len(tiempo_experimento)

print("\n--- ERROR CUADRÁTICO MEDIO ---")
print(f"ECM Cuadrático: {ecm_cuad:.6f}")
print(f"ECM Cúbico: {ecm_cub:.6f}")
print(f"ECM Exponencial: {ecm_exp:.6f}")

# --- 5. GRÁFICA (Punto 4) ---
plt.figure(figsize=(10, 6))
plt.plot(tiempo_experimento, altura_normalizada, 'rx', label='Datos (Exp)')
plt.plot(tiempo_experimento, y_fit_cuad, 'b-', label='Ajuste Cuadrático')
plt.plot(tiempo_experimento, y_fit_cub, 'm:', label='Ajuste Cúbico')
plt.plot(tiempo_experimento, y_fit_exp, 'g--', label='Ajuste Exponencial')

plt.title("Ajuste por Cuadrados Mínimos (Matricial) - Pomelo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura Normalizada (h/h0)")
plt.legend()
plt.grid(True)
plt.show()