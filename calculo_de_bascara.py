#Equação do segundo grau

print("insira o valor de A: ") 
A = int(input())

print("insira o valor de B")

B = int(input())

print("insira o valor de C")
C = int(input())

delta = (B*B)-4*A*C

print("O seu delta é:", delta)

#calculo das raízes

raizdelta = delta**0.5

print("Raiz do delta é:", raizdelta)

Raiz1 = int((((-1)*B) + (raizdelta))/(2*A))
Raiz2 = int((((-1)*B) - (raizdelta))/(2*A))

print("as raizes do sistema são:",Raiz1,"e", Raiz2 )


import matplotlib.pyplot as plt
import numpy as np

# Coeficientes da equação do segundo grau: ax^2 + bx + c
a = A
b = B
c = C

# Gerar valores de x
x = np.linspace(-10, 10, 100)

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