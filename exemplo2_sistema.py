#sistema de desconto de veiculo

#solicite o nome do veiculo

#solicite o preço do carro

#se o preço > 80 miil , 60 por cento de desconto
# se re

print("Qual o nome do carro?")
carro = str(input())

print("Qual o valor do carro?")
valor = float(input())

if valor >= 80000:
    carro80 = valor*0.4
    print("valor do", carro, "com desconto de 60% é:", carro80)
    desconto60 = valor*0.6
    print("o valor do desconto foi de:", desconto60)
elif 79999 > valor >= 50000:
    carro30 = valor*0.7
    print("valor do carro", carro, "com desconto de 30% é", carro30)
    desconto30 = valor*0.3
    print("o desconto foi de:", desconto30)
elif valor <= 30000:
    print("não existe desconto e o valor é:", valor)    
        
