import numpy as np

# 1. Datos de entrada (22 mediciones)
t = np.array([0, 0.83, 1.67, 2.5, 3.33, 4.13, 5, 5.83, 6.67, 7.5, 8.6, 
              9.17, 10, 10.83, 11.67, 12.5, 13.33, 14.17, 15, 15.83, 16.67, 17.5])

y = np.array([1.000, 0.951, 0.868, 0.810, 0.745, 0.665, 0.600, 0.557, 0.495, 
              0.431, 0.382, 0.329, 0.305, 0.271, 0.231, 0.194, 0.148, 0.123, 
              0.111, 0.077, 0.059, 0.052])

n = len(t)

# 2. Funciones base para el modelo cuadrático: y = a*1 + b*t + c*t^2
fi0 = np.ones(n)
fi1 = t
fi2 = t**2

# 3. Armado de la Matriz de Diseño (M) usando productos internos
# Esta es la matriz que vimos en tu captura de pantalla
M = np.array([
    [np.inner(fi0, fi0), np.inner(fi0, fi1), np.inner(fi0, fi2)],
    [np.inner(fi1, fi0), np.inner(fi1, fi1), np.inner(fi1, fi2)],
    [np.inner(fi2, fi0), np.inner(fi2, fi1), np.inner(fi2, fi2)]
])

# 4. Vector de términos independientes (b)
b_ind = np.array([
    np.inner(fi0, y),
    np.inner(fi1, y),
    np.inner(fi2, y)
])

# 5. Resolución del sistema para hallar los coeficientes [a, b, c]
coef = np.linalg.solve(M, b_ind)

print(f"Coeficientes: a = {coef[0]:.4f}, b = {coef[1]:.4f}, c = {coef[2]:.4f}")

# 6. Cálculo del Error Cuadrático Medio (ECM)
y_ajustado = coef[0]*fi0 + coef[1]*fi1 + coef[2]*fi2
error = y - y_ajustado
ECM = np.sqrt(np.inner(error, error) / n)

print(f"ECM Final = {ECM:.6f}")