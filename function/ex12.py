#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(year):
    a = date.today().year
    if a - year < 16:
        return 'NEGADO'
    elif a - year >= 16 and a - year < 18:
        return 'Opicional'
    else:
        return 'Voto obrigatório'

#-------------------------------------------------------------------------------------------------------------------------

ano = int(input("Informe o ano de nascimento: "))                

print (voto(ano))