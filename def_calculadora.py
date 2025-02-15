
def menu():
    print("Menu da claculadora")
    print("1 - somar")
    print("2 - subtrair")
    print("9 - Sair")
    
def somar(n1, n2):
    return n1+n2

def subtracao(n1, n2):
    return n1-n2

def verificaOpcao(opcao):
    if opcao == 1:
        num1 = float(input("digite o numero 1\n"))
        num2 = float(input("digite o numero 2\n"))
        print(somar(num1, num2))
    elif opcao == 2:
        num1 = float(input("digite o numero 1\n"))
        num2 = float(input("digite o numero 2\n"))
        print(subtracao(num1, num2))
    else:
        print("fim")
        
def calculadora():
    while True:
        menu()
        opcao = int(input("escolha uma opção"))
        verificaOpcao(opcao)
        
calculadora()



