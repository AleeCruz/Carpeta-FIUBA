import matplotlib.pyplot as plt
import numpy as np

# Constantes
R = 0.05  # 5 cm
lam = 0.1e-6  # 0.1 uC/m
eps0 = 8.854e-12

# Distancia z (de -20 cm a 20 cm)
z = np.linspace(-0.2, 0.2, 1000)

# Campo eléctrico E(z)
E = (lam * R * z) / (2 * eps0 * (R**2 + z**2) ** 1.5)

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(z * 100, E, label="Campo Eléctrico $E(z)$", color="blue")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.xlabel("Distancia $z$ (cm)")
plt.ylabel("Campo Eléctrico $E$ (N/C)")
plt.title("Campo Eléctrico en el eje de un anillo cargado")
plt.grid(True)
plt.legend()
plt.show()