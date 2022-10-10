def cadastro():
    nome = str(input("What's your name? "))
    age = int(input('how old are you?'))
    return nome,age

#-------------------------------------------------------------------------------------------------------------------------

nome,age = cadastro()    

print (f"Seu nome é {nome}\nSua idade é de {age} anos")