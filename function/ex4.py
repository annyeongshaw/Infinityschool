#Faça um procedimento que recebe 3 valores inteiros por parâmetro e retorna-os ordenados em ordem crescente.

lis = []

for i in range(3):
    n = int(input("Informe a variável: "))
    lis.append(n)

print(sorted(lis))