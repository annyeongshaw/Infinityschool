#Elaborar um algoritmo que captura 10 valores inteiros na tela e adicione-os em uma lista. Exiba apenas os ímpares.

impares=[]
for i in range(10):
    n = int(input("Enter an integer: "))
    if n%2!=0:
        impares.append(n)
print('-'*100)
for impar in impares:
    print(impar,end=' ')
      
     