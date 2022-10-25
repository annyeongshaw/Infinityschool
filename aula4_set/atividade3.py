#Refaça o programa anterior, mas desta vez, para 7 alunos e imprima na tela todos os dados dos alunos

for i in range(7):
  notas=[]
  nome =  input("Qual é o seu nome: ")
  for i in range(1,5):

    notas.append(float(input(f"Informe a {i}° nota: ")))
  media = sum(notas)/4
  if media < 7:
      situacao = str('Reprovado')
  else:
      situacao = str('Aprovado')
  aluno = {
    'Nome' : nome,
    'Notas' : notas,
    'maior nota' : max(notas),
    'Menor nota' : min(notas),
    'Média' : media,
    'Situação' : situacao
  }  
  print('\n\n' ,'-'*100)
  for d,v in zip(aluno.keys(),aluno.values()):
    print(d,v,sep='- ')
  print('-'*100)    
  aluno = dict.fromkeys(aluno)
  print("Outro aluno:\n")