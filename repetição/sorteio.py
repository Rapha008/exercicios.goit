import random

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Lista inicio: ", numeros)
random.shuffle(numeros)
print("Depois do sorteio: ", numeros)
print('Resultado final: ', sorted(numeros[0:10]))


