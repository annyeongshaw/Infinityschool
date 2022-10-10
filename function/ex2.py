#Elaborar um algoritmo que calcule a área de triângulos , quantos o usuário quiser calcular separe a função com o nome “calcula_triangulo”.

def calcula_triangulo (a,b):
    "Calcula a area do triangulo"
    return (a*b)/2 

#-----------------------------------------------------------------------------------------------------------------------
while True:
    base = float(input("Informe a base do triângulo: "))
    altura = float(input("Informe a altura do triângulo: "))
    print (f"A área do triângulo é {calcula_triangulo(base,altura)}")
    sair = str(input("Deseja a área de mais algum triângulo ,responda com sim ou não?" ))
    if sair == 'sim':
        continue
    else:
        break

print (print .__doc__)