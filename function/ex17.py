#Modifique o programa anterior para a nova impressão ser:
#1
# 1   2
# 1   2   3
# .
# .
# .
# 1   2   3   4   ...   n

def piramide (int):
    print('-'*100)
    for linha in range(1,int+1):
        for i in range(1,linha+1):
            print(i , end='  ')
        print('')    
       
    return ('-'*100)

n = int(input("Informe a altura da piramide: "))
print (piramide(n)) 