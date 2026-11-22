import matplotlib.pyplot as plt
import numpy as np

# 1. Valores posibles de Y y sus probabilidades p_Y(y)
y_values = np.array([-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0])
probabilities = np.array([0, 1/36, 1/18, 1/12, 1/9, 5/36, 1/6, 7/36, 2/9])

# Etiquetas en formato de fracción para el eje horizontal
y_labels = [r'$-1$', r'$-\frac{3}{4}$', r'$-\frac{1}{2}$', r'$-\frac{1}{4}$', 
            r'$0$', r'$\frac{1}{4}$', r'$\frac{1}{2}$', r'$\frac{3}{4}$', r'$1$']

# 2. Configurar la figura
plt.figure(figsize=(9, 5))

# Graficar el diagrama de bastones (stem plot)
markerline, stemlines, baseline = plt.stem(y_values, probabilities, basefmt=" ")

# Estilizar las líneas y puntos
plt.setp(markerline, color='#1f77b4', markersize=7)
plt.setp(stemlines, color='#1f77b4', linewidth=2)

# Añadir la línea horizontal de cero
plt.axhline(0, color='gray', linewidth=1, linestyle='--')

# 3. Configuración de ejes y etiquetas
plt.xticks(y_values, y_labels, fontsize=11)
plt.xlabel('Valores de $Y$ ($y = 2x - 1$)', fontsize=12, labelpad=10)
plt.ylabel('Probabilidad Puntual $p_Y(y)$', fontsize=12, labelpad=10)
plt.title('Función de Probabilidad Puntual $p_Y(y)$ para $Y = 2X - 1$', fontsize=13, fontweight='bold', pad=15)

# Limites del eje Y con margen superior
plt.ylim(-0.01, 0.26)
plt.grid(axis='y', linestyle=':', alpha=0.7)

# Mostrar etiquetas numéricas/fraccionarias sobre cada bastón
frac_labels = ['0', r'$\frac{1}{36}$', r'$\frac{1}{18}$', r'$\frac{1}{12}$', 
               r'$\frac{1}{9}$', r'$\frac{5}{36}$', r'$\frac{1}{6}$', r'$\frac{7}{36}$', r'$\frac{2}{9}$']

for y_val, prob, label in zip(y_values, probabilities, frac_labels):
    plt.annotate(label, (y_val, prob), textcoords="offset points", 
                 xytext=(0, 6), ha='center', fontsize=9.5, color='#333333')

# Ajustar diseño y mostrar
plt.tight_layout()
plt.show()