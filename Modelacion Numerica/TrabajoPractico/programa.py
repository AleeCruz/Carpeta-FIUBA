import numpy as np

# Entrada de datos
h = np.array([
    10.249, 9.745, 8.893, 8.299, 7.632, 6.812, 6.151, 5.711,
    5.078, 4.415, 3.911, 3.376, 3.128, 2.775, 2.366, 1.987,
    1.514, 1.262, 1.136, 0.788, 0.600, 0.537, 0.441, 0.315,
    0.161
])

t = np.array([
    0, 0.83, 1.67, 2.5, 3.33, 4.13, 5.00, 5.83, 6.67, 7.50,
    8.60, 9.17, 10.0, 10.83, 11.67, 12.5, 13.33, 14.17,
    15.0, 15.83, 16.67, 17.5, 18.33, 19.17, 20.0
])

# normalizo la altura
h0 = h[0]
y = h / h0

# linealizo con logaritmo
Y = np.log(y)

# cantidad de datos
n = len(t)

# funciones base
fi0 = np.ones(n)
fi1 = t

# armo la matriz

M = (
    np.inner(fi0, fi0),
    np.inner(fi0, fi1),
    np.inner(fi1, fi0),
    np.inner(fi1, fi1)
)

M = np.array(M).reshape((2,2))



b = (
    np.inner(fi0, Y),
    np.inner(fi1, Y)
)

b = np.array(b).reshape((2,1))


c = np.linalg.inv(M) @ b

# extraigo los coeficientes
a = c[0,0]
b_coef = c[1,0]

print("a =", a)
print("b =", b_coef)

# armo el modelo ajustado la parte de potencia

Yt = a * fi0 + b_coef * fi1

# vuelvo al modelo exponencial
y_ajustado = np.exp(Yt)

# --- ERROR CUADRATICO MEDIO ---

dif = y - y_ajustado

ECM = np.sqrt(np.inner(dif, dif) / n)

print("ECM =", ECM)