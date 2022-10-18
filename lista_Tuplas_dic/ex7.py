# 2) Aproveitando a lista do exercício 1, imprima uma tabela em que na primeira coluna imprima os 100 valores da lista, na segunda coluna imprima o dobro de cada valor e na terceira coluna imprima seu antecessor inteiro.
#    Exemplo:
#       1   2   0
#       2   4   1
#       3   6   2
listaNumNaturais = list(range(1,101))
print('(%s) (%s) (%s) ' % ('100 valores','dobro',('antecessor')))
for i in listaNumNaturais:
    print('%5d %12d %10d' % (i, i*2, i-1))