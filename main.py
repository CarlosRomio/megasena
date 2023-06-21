import random
tentativas = 0
numeros = []
indice = None
while True:
    aposta = input("informe um número da sua aposta: ")
    aposta = [int(aposta)]
    if len(numeros) > 0:
        indice = int(len(numeros)) -1
        print(numeros)
        print(aposta)
        if aposta == numeros[indice]:
            aposta = ''
            print("Número já inserido")
    elif aposta >= [61]:
        aposta = ""
        print("Insira números menores que 60")
    if aposta != "":
        numeros += aposta
    if len(numeros) ==  6:
        break


def ordenar(x):
	x.sort()
	

ordenar(numeros)
while True:
    numeros_sorteados = random.sample(range(1, 61), 6)
    ordenar(numeros_sorteados)
    tentativas = tentativas + 1
    if numeros == numeros_sorteados:
         print("Parabéns você acertou")
         print('O número de tentativas necessárias foi: ', tentativas)
         break
