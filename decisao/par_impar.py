numero = float(input("Digite um numero para sabermos se ele é impar ou par:   "))
resto = numero % 2

if resto == 0:
    print("O número é par! ")
else:
    print("O número é ímpar!")