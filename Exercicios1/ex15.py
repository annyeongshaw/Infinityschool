#Você foi contratado pela prefeitura para criar um programa que calcule a quantidade de água desperdiçada em vazamentos de água por toda a cidade. O programa deve receber a quantidade de vazamentos notificados a prefeitura no dia e para cada um deles deve pedir a quantidade de horas que o vazamento ficou aberto e ao final da execução exibir o total de água desperdiçada. exemplo: vazamentos 2. litros por hora : 10 horas : 2. litros por hora :4horas:1 . saída 24 litros
quatidadeVazamentos = int(input("Informe quantos vazamentos foram identificados na atual data: "))

total = 0

for i in range (quatidadeVazamentos):

    print("-"*50)

    quantidade = int(input("Informe a quantidade de litros desperdiçados por hora: "))

    horas = int(input("Informe a quantidade de horas que o vazamento ficou aberto: "))

    total += quantidade * horas

print(f"Foram desperdiçados {total} litros")    