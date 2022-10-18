#Escreva uma função que receba dois parâmetros, sendo o primeiro um número inteiro e o segundo uma porcentagem, depois calcule e retorne o valor do número somado ao aumento percentual informado.

def aumento (val1,perc):
    val1 = (val1*perc)/100 + val1 
    return val1



n1= int(input("Informe um valor: "))
per = float(input("Informe a porcentagem: "))

print(aumento(n1,per))
    