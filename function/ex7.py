# Escreva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite
def sum_limite(a,b,limite):
    if (a + b) > limite:
        return True
    else:
        return False 

#-------------------------------------------------------------------------------------------------------------------------

x = float(input('Informe o primeiro valor: '))
y = float(input('Informe o segundo valor: '))
limite = int(input('Informe o limite da soma: ')) 

print(sum_limite(x,y,limite))
