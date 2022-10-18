#Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
def sum (a):
    x = 0
    for i in range (a+1):
       x = x+i
    return x
#---------------------------------------------start the program here------------------------------------------------------

n = int(input("Informe uma variável: "))

print(sum(n))    



