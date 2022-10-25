#Leia 4 notas de um aluno, calcule sua média e armazene em um dicionário as seguintes informações:
# * Nome do aluno
# * As 4 notas obtidas
# * Maior nota
# * Menor nota
# * Média
# * Situação
# * Aprovado se média for maior ou igual a 7
# * Reprovado se média for menor que 7
# Agora imprima as informações deste aluno na saída padrão

"""Minha versão"""
notas=[]
for i in range(1,5):
    notas.append(int(input(f"Informe a {i}° nota: ")))

media = sum(notas)/4
if media < 7:
    situacao = str('Reprovado')
else:
    situacao = str('Aprovado')
aluno = {
    'Nome' : input("Qual é o seu nome: "),
    'Notas' : notas,
    'maior nota' : max(notas),
    'Menor nota' : min(notas),
    'Média' : media,
    'Situação' : situacao
} 
print('-'*100)
for d,v in zip(aluno.keys(),aluno.values()):
    print(d,v,sep='- ')
print('-'*100)    