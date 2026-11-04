import numpy as np
import matplotlib.pyplot as plt

def graficar_campo_electrico_disco():
    # ---------------------------------------------------------
    # 1. Definición de Parámetros Físicos (Valores del ejercicio)
    # ---------------------------------------------------------
    R_cm = 30.0               # Radio en cm
    Q_uC = 0.2                # Carga total en micro-Coulombs
    epsilon0 = 8.854e-12      # Permitividad del vacío en C^2/(N*m^2)

    # Convertir a unidades del Sistema Internacional (SI)
    R = R_cm / 100.0          # m
    Q = Q_uC * 1e-6           # C

    # Calcular densidades y constantes
    area = np.pi * R**2       # m^2
    sigma = Q / area          # C/m^2
    constante_E = sigma / (2 * epsilon0) # V/m

    # Imprimir valores para verificación
    print(f"--- Parámetros Calculados ---")
    print(f"Radio (R): {R} m")
    print(f"Densidad de carga (sigma): {sigma:.4e} C/m^2")
    print(f"Constante sigma/(2*epsilon0): {constante_E/1000:.2f} kV/m")

    # ---------------------------------------------------------
    # 2. Definición de la Función del Campo Eléctrico E_z(z)
    # ---------------------------------------------------------
    def campo_z(z_m):
        """
        Calcula la componente z del campo eléctrico en el eje.
        Entrada: z_m (posición en metros, puede ser un array de numpy).
        Salida: E_z (campo en V/m).
        """
        # Usamos np.where para manejar el salto en z=0 de forma segura con arrays
        # sgn(z) * [ 1 - |z| / sqrt(R^2 + z^2) ]
        
        term_raiz = np.abs(z_m) / np.sqrt(R**2 + z_m**2)
        # sgn es +1 para z>0, -1 para z<0, 0 para z=0
        sgn_z = np.sign(z_m)
        
        Ez = constante_E * sgn_z * (1.0 - term_raiz)
        return Ez

    # ---------------------------------------------------------
    # 3. Preparación de Datos para la Gráfica
    # ---------------------------------------------------------
    # Definimos el rango de visualización en cm para el eje X
    rango_vista_cm = 80.0
    
    # Creamos un array de puntos para z (en cm)
    # Usamos muchos puntos para que la curva se vea suave.
    z_grafica_cm = np.linspace(-rango_vista_cm, rango_vista_cm, 1000)
    
    # IMPORTANTE: Para graficar correctamente la discontinuidad en z=0,
    # no debemos incluir el punto exacto 0, o manejarlo por separado.
    # Una forma sencilla es usar dos arrays, uno para z < 0 y otro para z > 0.
    
    z_neg_cm = np.linspace(-rango_vista_cm, -0.01, 500) # De -80 a casi 0
    z_pos_cm = np.linspace(0.01, rango_vista_cm, 500)  # De casi 0 a 80

    # Convertir a metros para el cálculo
    z_neg_m = z_neg_cm / 100.0
    z_pos_m = z_pos_cm / 100.0

    # Calcular el campo para ambas regiones (en V/m)
    Ez_neg = campo_z(z_neg_m)
    Ez_pos = campo_z(z_pos_m)

    # Convertir el resultado a kV/m para una escala más legible en el eje Y
    Ez_neg_kV = Ez_neg / 1000.0
    Ez_pos_kV = Ez_pos / 1000.0

    # ---------------------------------------------------------
    # 4. Creación de la Gráfica con Matplotlib
    # ---------------------------------------------------------
    # Configurar el tamaño de la figura
    plt.figure(figsize=(10, 6))

    # Graficar la región z < 0
    plt.plot(z_neg_cm, Ez_neg_kV, color='blue', linewidth=2.5, label=r'$E_z(z)$')
    
    # Graficar la región z > 0 (con el mismo color)
    plt.plot(z_pos_cm, Ez_pos_kV, color='blue', linewidth=2.5)

    # --- Estilo y Etiquetas ---
    
    # Título principal y etiquetas de los ejes (con formato LaTeX)
    plt.title(f'Campo Eléctrico $E_z$ en el eje de un Disco Cargado\n'
              f'($Q = {Q_uC}\ \mu C$, $R = {R_cm}\ cm$)', fontsize=14)
    plt.xlabel('Posición en el eje, $z$ (cm)', fontsize=12)
    plt.ylabel('Componente $E_z$ (kV/m)', fontsize=12)

    # Añadir líneas de los ejes X e Y principales (en gris, discontinuas)
    plt.axhline(0, color='gray', linestyle='--', linewidth=1)
    plt.axvline(0, color='gray', linestyle='--', linewidth=1)

    # Configurar los límites de los ejes para que se vea bien
    lim_y = constante_E / 1000.0 * 1.1 # Un 10% más arriba del máximo
    plt.ylim(-lim_y, lim_y)
    plt.xlim(-rango_vista_cm, rango_vista_cm)

    # Añadir una cuadrícula de fondo
    plt.grid(True, which='both', linestyle=':', alpha=0.6)

    # Añadir anotaciones para puntos clave
    valor_max_kV = constante_E / 1000.0
    # Anotación en z = 0^+
    plt.annotate(f'+{valor_max_kV:.1f} kV/m', 
                 xy=(0, valor_max_kV), xytext=(10, valor_max_kV*0.8),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
    # Anotación en z = 0^-
    plt.annotate(f'-{valor_max_kV:.1f} kV/m', 
                 xy=(0, -valor_max_kV), xytext=(-35, -valor_max_kV*0.8),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

    # Mostrar una leyenda (opcional aquí, ya que solo hay una curva)
    # plt.legend()

    # Ajustar el diseño para que no se corten las etiquetas
    plt.tight_layout()

    # Mostrar la gráfica
    print("\nMostrando gráfica...")
    plt.show()

if __name__ == "__main__":
    graficar_campo_electrico_disco()