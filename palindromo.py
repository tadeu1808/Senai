#verfficar se umapalavara é um palidromo

#é palindromo ou não é palindromo
#case sensitive


print("insira a palavra:")
palavra = str(input())

if palavra == palavra[::-1]:
   
    print("É um Palindromo")
    print("a palavra invertida é:", palavra[::-1])
else:
    print("Não é Palindromo") 
    print("a palavra invertida é:", palavra[::-1])
    
    
#coreto:
    
# palavra = input().lower().strip().replace(" ","")

