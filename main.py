from random import random
numeros = []
while True:
    aposta = input("informe um número da sua aposta: ")
    if len(aposta) == 1:
        aposta = "0" + aposta
    elif aposta in numeros:
        aposta = ''
        print("Número já inserido")
    elif int(aposta) >= 61:
        aposta = ""
        print("Insira números menores que 60")
    if aposta != "":
        aposta = [aposta]
        numeros += aposta
    if len(numeros) ==  6:
        break


def ordenar(x):
	x.sort()
	for i in x:
		print(i)

ordenar(numeros)


sorteio = random.randrange(1,60)

print(sorteio)

#pipipi popopo
