#Leia os dados de um usuário - nome, sobrenome, idade, email - e imprima-os enumerando os mesmos.
"""Minha solução"""
dados = {
    'nome' : str(input("Qual é seu nome: ")),
    'sobrenome': str(input("Qual seu sobrenome: ")),
    'idade' : int(input('Informe sua idade: ')),
    'Email' : str(input("Informe seu email: "))
}
print('-'*50)
dados1,valores= dados.keys(),dados.values()
for dados1,valores in zip(dados1,valores):
    print(dados1,valores,sep=' - ')

#solução do professor 
""" dados = {}

nome = input('Nome: ').strip().title()
sobrenome = input('Sobrenome: ').strip().title()
idade = int(input('Idade: '))
email = input('Email: ').strip().lower() """

# Forma 1
#dados['Nome'] = nome
#dados['Sobrenome'] = sobrenome
#dados['Idade'] = idade
#dados['E-mail'] = email

# # Forma 2
# dados['Nome'] = input('Nome: ')
# dados['Sobrenome'] = input('Sobrenome: ')
# dados['Idade'] = int(input('Idade: '))
# dados['E-mail'] = input('Email: ')

# # Forma 3
# dados['Nome'], dados['Sobrenome'], dados['Idade'], dados['Email'] = nome, sobrenome, idade, email

# # Forma 4
# dados = {
#     'Nome' : input('Nome: '),
#     'Sobrenome' : input('Sobrenome: '),
#     'Idade' : int(input('Idade: ')),
#     'E-mail' : input('Email: ')
# }

