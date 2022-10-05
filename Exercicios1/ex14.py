exE = int(input("Informe o extremo esquerdo: ")) 

exD = int(input("Informe o extremo direito: ")) #Como é um intervalo do tipo aberto e limitado. usei a nomeclatura extremo esquerdo e extremo direito.

numerosPrimos = list()

for i in range(exE, exD):

    if exE > 1:

        for i in range(2, exE):

            if exE % i == 0:

                break

        else:

            numerosPrimos.append(exE)

    exE += 1

print(f"Os números primos presentes no intervalo são: {numerosPrimos}")