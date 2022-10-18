#Crie uma função que dado uma data digitada pelo usuário, informe há quantos dias atrás aconteceu aquela data.
from datetime import date

def calculador_dias(day,month,year):
    data_antiga = date(year,month,day)
    dat = date.today()
    return (dat - data_antiga).days
#-------------------------start the program here --------------------------------------------

day = int(input("informe o dia: "))
month = int(input("informe o mês: "))
year = int(input("informe o ano: "))

print (calculador_dias(day,month,year))


