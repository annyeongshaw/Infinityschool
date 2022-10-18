#Crie um programa que lê 10 caracteres e os insere em uma lista. Após, elabore uma função que retorne a quantidade de consoantes que há nessa lista.

def numero_Consoantes(lista):
    x= len(lista)
    for i in lista:
        if i in 'aeiouAEIOU':
            x-=1
    return x        

integer=[]
for i in range(10):
    integer.append(input("Informe um caracter: "))
print(numero_Consoantes(integer))
    