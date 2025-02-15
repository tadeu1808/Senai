#Equação do segundo grau

print("insira o valor de A")
A = int(input())

print("insira o valor de B")

B = int(input())

print("insira o valor de C")
C = int(input())

delta = (B*B)-4*A*C

print("o seu delta é:", delta)

#calculo das raízes

raizdelta = delta**0.5

print("raiz do delta:", raizdelta)

Raiz1 = int((((-1)*B) + (raizdelta))/(2*A))
Raiz2 = int((((-1)*B) - (raizdelta))/(2*A))

print("as raizes do sistema são:",Raiz1,"e", Raiz2 )


