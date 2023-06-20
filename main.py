import random
numeros = []
while True:
    aposta = input("informe um número da sua aposta: ")
    if aposta in numeros:
        aposta = ''
        print("Número já inserido")
    elif int(aposta) >= 61:
        aposta = ""
        print("Insira números menores que 60")
    if aposta != "":
        aposta = [int(aposta)]
        numeros += aposta
    if len(numeros) ==  6:
        break


def ordenar(x):
	x.sort()
	

ordenar(numeros)
while True:
    numeros_sorteados = random.sample(range(1, 61), 6)
    ordenar(numeros_sorteados)
    if numeros == numeros_sorteados:
         print("Parabéns você acertou")
         break
