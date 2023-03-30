nome = input("Digite seu nome:  ")
sal = float(input("Digite seu salario:  "))
temp = int(input("Quantos anos você trabalha nesta trabalha: "))

if temp <= 3:
    print("Seu novo sálario é:  ", sal+sal*0.03)
if temp > 3 <= 10:
    print("Seu novo sálario é:  ", sal+sal*0.12)
if temp >= 10:
    print("Seu novo sálario é:  ", sal+sal*0.20)