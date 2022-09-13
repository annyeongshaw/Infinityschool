""" 2. Ler 3 valores (considere que não serão informados valores iguais) 
e escrevê-los em ordem crescente """

val1 = float(input("Informe o primeiro valor: "))
val2 = float(input("Informe o segundo valor: "))
val3 = float(input("Informe o terceiro valor: "))

if val1 > val2 and val2 > val3:
    print ("-"*50)
    print (val3,val2,val1,sep = ", ")
elif val1 > val3 and val3 > val2:
    print ("-"*50)
    print(val2,val3,val1,sep = (", "))
elif val2 > val1 and val1 > val3:
    print ("-"*50)
    print(val3,val1,val2,sep = (", "))
elif val2 > val3 and val3 > val1:
    print ("-"*50)
    print(val1,val3,val2,sep = (", "))
elif val3 > val1 and val1 > val2:
    print ("-"*50)
    print(val2,val1,val3,sep = (", "))
else:
    print ("-"*50)
    print(val1,val2,val3,sep = (", "))        

