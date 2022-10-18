#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você é um "natural" e venceu o jogo. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
from random import randint

jogada = str(input("Deseja lançar os dados ?\tsim ou não:  "))
if jogada == 'sim':
    dado1=randint(1,6)
    dado2=randint(1,6)
    soma = dado1 + dado2
    if soma == 7 or soma == 11:
        print("Você venceu o jogo. Parabéns!!!")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Você perdeu")
    elif soma == range(4,11):
        while True:
            dado1=randint(1,6)
            dado2=randint(1,6)
            soma2 = dado1+dado2
            if soma2 == 7:
                print("Você perdeu")
                break
            if soma == soma2:
                print("Você venceu o jogo.")
                break
            
                 
