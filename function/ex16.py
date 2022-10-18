#Faça um programa que receba um número por parâmetro e apresente em tela a seguinte impressão:
# 1
# 2   2
# 3   3   3
# .
# n   n   n   n   n

""" def piramide (int):
    for i in range(int):
        i += 1
        print("  ".join(str(i)*i))
    return ''

n = int(input("Informe a altura da piramide: "))
print (piramide(n))   """      

def piramide (int):
    print('-'*100)
    for i in range(int):
        i += 1
        print((' '.join(str(i)*i)))
    return ('-'*100)   
    

n = int(input("Informe a altura da piramide: "))
print (piramide(n)) 