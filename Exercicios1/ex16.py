# você foi contratado para desenvolver um programa similar ao funcionamento do waze (navegador de bordo). Ele terá que calcular a distância percorrida pelo automóvel considerando as direções (siga em frente, vire a esquerda,  vire a direira ou pare ) O programa deve receber um número indefinido de direções que o está seguindo e a cada uma delas atribui-se o valor percorrido de 100. Quando for digitado parar, o programa deve exibir distância percorrida em Km. exemplo: siga em frente, vire a esquerda, vire a direita,diga em frente e pare . saída 0,4 km 
distancia = 0

while True:

    direcao = str(input("Informe quais direções abaixo deseja seguir:\n1- Siga em frente\n2- Vire a esquerda\n3- Vire a direita\n4- Parar\nEscreva a direção desejada: ")).lower().replace(' ','')

    if direcao == "sigaemfrente":

        distancia += 100

    elif direcao == "vireaesquerda":

        distancia += 100

    elif direcao == "vireadireita":

        distancia += 100

    elif direcao == 'parar':

        break

    else:

        print("-"*50)

        print ("Você digitou errado.Tente novamente.")

        print("-"*50)

        continue            

print (f"A distância percorrida foi {distancia/1000} km")