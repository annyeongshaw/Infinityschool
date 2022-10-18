def SuperSoma(lista:list=[0]):
    soma=0
    for i in lista:
        soma = soma + i; 
    return soma  
# Testando a função...
print("Somatório do preço de todas as mercadorias: ")
print( SuperSoma([12.50, 35.00, 25.40, 27.10]) ) # 100.0
print("Usando a função SuperSoma() sem argumentos: ")
print( SuperSoma() )