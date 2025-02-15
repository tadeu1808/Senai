import matplotlib.pyplot as plt
import numpy as np

# Coeficientes da equação do segundo grau: ax^2 + bx + c
a = 1
b = -3
c = 2

# Gerar valores de x
x = np.linspace(-10, 10, 400)

# Calcular valores de y com base na equação do segundo grau
y = a * x**2 + b * x + c

# Criar o gráfico
plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Equação do Segundo Grau')
plt.legend()

# Exibir o gráfico
plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()
