#Refaça o programa anterior e imprima a lista dos alunos aprovados em ordem decrescente da maior média para a menor
lisMedia=[]
for i in range(2):
  notas= []
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
  if situacao == 'Aprovado':
    lisMedia.append(aluno['Média'])
  aluno = dict.fromkeys(aluno)
  print("Outro aluno:\n")
lisMedia.sort(reverse=True)
print("Lista da maior média para a menor média:")
for i in lisMedia:
    print(i,end=' ')
