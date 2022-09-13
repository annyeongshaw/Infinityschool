""" 1. Ler 3 valores (considere que não serão informados valores iguais) 
e escrever a soma dos 2 maiores. """

lista = []
for i in range (1,4):
    n = int(input("Informe um número inteiro: "))
    lista.append(n)

x = sorted(lista)
print (x)
print (sum(x)-x.pop(0))    
