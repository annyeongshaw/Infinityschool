#Escreva uma função que receba um nome como parâmetro e informe quantas vogais existem nele.

""" def contador_Vogais(string):
    x = string.count('a')+string.count('e')+string.count('i')+string.count('o')+string.count('u')
    x1 = string.count('A')+string.count('E')+string.count('I')+string.count('O')+string.count('U')
    return x + x1

name=str(input("Informe seu nome: "))
print(contador_Vogais(name))     """

def contador_Vogais(string):
    nV = 0
    vogais = set('aeiouAEIOU')
    for al in string:
        if al in vogais:
            nV += 1
    return nV   


name = str(input("Informe um nome: "))
print (contador_Vogais(name))         