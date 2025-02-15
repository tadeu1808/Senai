# função Def


def carro():
    print("peugeot 206")
    print("citroen zx")
    print("picasso")
    
carro()
carro()



def escrever_carro(nome):
    print(nome)
    
escrever_carro("marea turbo")


def somar_numeros(num1, num2):
    return num1 + num2
resultado = somar_numeros(4,4)
print("o resultado é: ", resultado)



def verifica_idade(idade):
    if idade >= 18:
        return "pode ver o filme"
    else:
        return "não pode ver o filme"
print("digite sua idade:")
idade = int(input())

resultado = verifica_idade(idade)

print(resultado)




