#Fizz Buzz - Se o parâmetro da função for divisível por 3 , retorne fizz, se o parâmetro da função for divisível por 5, retorne buzz. se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.

def fizz_buzz(x):
    if x%3==0 and x%5==0:
        return 'FizzBuzz'
    elif x%5==0:
        return 'Buzz'
    elif x%3==0:
        return 'Fizz'
    else:
        return x 

#-------------------------------------------------------------------------------------------------------------------------                   
n = int(input("Informe um valor: "))
print(fizz_buzz(n))