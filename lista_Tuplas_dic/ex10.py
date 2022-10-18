#Crie um programa que leia 20 números inteiros digitados pelo usuário, depois, crie uma função que recebe esta lista e gere 2 listas, uma com os valores pares e outra com os ímpares. Imprimir as 3 listas.

def analise(lista):
    impares = []
    pares = []
    print(len(lista))
    for inteiro in lista:
        if inteiro%2==0:
            pares.append(inteiro)
        else:
            impares.append(inteiro) 
    return [impares,pares]

lis = []
for inter in range(20):
    n = int(input("Informe um número inteiro: "))
    lis.append(n)           
impares,pares = analise(lis)
print(f"Números impares: {impares}")
print(f"Números pares: {pares}\n",f'lista: {lis}')
