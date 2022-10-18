#Escreva um programa que receba três argumentos. Dois valores e umoperador. E realize a operação entre os dois valores passados deacordo com o operador fornecido pelo usuário (soma, subtração,divisão, multiplicação).

def computador(val1,val2,operador):
    if operador == '+':
        return (val1 + val2)
    elif operador == '-':
        return (val1 - val2)
    elif operador == '*':
        return (val1 * val2)
    else:
        return (val1 / val2)             


#------------------------------------------------------------------------------------------------------------------------- 
n1 = float(input("Informe o primeiro valor: "))
n2 = float(input("Informe o segundo valor: "))
operador = str(input('Escolha dentre as opções baixo:\n1-(+)\n2-(-)\n3-(*)\n4-(/)\nEscolha: '))        
print (computador(n1,n2,operador))