#Elaborar um algoritmo que captura 5 nomes na tela e adicione em uma lista. Exiba-os em seguida

lis = []
for nome in range (5):
    name = str(input("Informe um nome: "))
    lis.append(name)
print('-'*100)
for i in lis:
    print('-',i)
print('-'*100)    