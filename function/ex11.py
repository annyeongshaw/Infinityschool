#Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def inversor (x):
    a = str(x)
    a = a[::-1]
    a = int(a)
    return a

#-------------------------------------------------------------------------------------------------------------------------

n = int(input("Informe o valor que será invertido: "))
print (inversor(n))

