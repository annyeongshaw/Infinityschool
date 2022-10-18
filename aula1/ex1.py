#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:  até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro;
# Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro. 
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90

total=0
QL = float(input("Informe a quantidade de litros vendidos: "))
tipo = str(input("Informe o tipo de combustível: A=álcool ou G-gasolina\nDigite a letra correspondente: ")).lower()

if QL <= 20 and tipo == 'a':
    total = QL * 1.9
elif QL <= 20 and tipo == 'g':
    total = QL * 2.5    
elif QL > 20 and tipo == 'a':
    total = (20*1.9) + ((QL-20)*1.9*95)/100
elif QL > 20 and tipo == 'g':
    total = (20*2.5) + ((QL-20)*2.5*94)/100    
else:
    pass
print('O total a ser pago:R$ %.3f'%(total))    