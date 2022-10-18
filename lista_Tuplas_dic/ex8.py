#Aproveitando a lista do ex.1, substitua todos os valores pares pelo caracter '*'
listaNumNaturais = list(range(1,101))
for num in range(0,len(listaNumNaturais)):
    if listaNumNaturais[num]%2==0:
        listaNumNaturais[num] = '*'
print(listaNumNaturais) 
for i in listaNumNaturais:
    print(i)       