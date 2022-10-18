#Crie um programa que irá sortear um número aleatório dentro de dois intervalos (início e fim) fornecidos pelo usuários, e retorne o número sorteado para o mesmo. Para isso, use a função. random.randrange(start, stop, step)

from random import randrange 

start = int(input('Informe o númeoro inicial: '))
end = int(input('Informe o numero final: '))

print(randrange(start,end),end=' ')
