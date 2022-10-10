#Crie um algoritmo em Python, que dado dois números informados pelo usuário e sua operação (das 4 operações básicas da matemática), realize os cálculos adequados dentro de funções.

def Calculador (a,b,c):
    if c == '+' or c == '-' or c == '*' or c == '/':
     if c == '+':
        return a+b
     elif c == '-':
        return a-b
     elif c == '*':
        return a*b 
     else:
        return a/b     
    else: 
        return "Não é uma das operações básicas. Tente novamente"

#-------------------------------------------------------------------------------------------------------------------------


n1 = float(input("Informe a primeira variável: "))
n2 = float(input("Informe a segunda variável: "))
Op = str (input("Informe uma das 4 operações abaixo:\n1. '-'\n2. '+'\n3. '*'\n4. '/'\nEscolha uma opção: "))
print (f"O resultado da operação é: {Calculador(n1,n2,Op)}")