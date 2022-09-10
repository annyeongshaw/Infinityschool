#Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o mesmo número de pontos, criar um programa que informe se uma equipe foi classificada, de acordo com a seguinte especificação: 
# • Ler os pontos obtidos por cada jogador da equipe; 
# • Mostrar esses valores em ordem decrescente; 
# • Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles, caso contrário, imprimir a mensagem "Equipe desclassificada". 

addition = 0
point = []
for i in range (1,4):
    points = int(input("Enter player points: "))
    point.append(points)
    addition += points
print (point.sort())