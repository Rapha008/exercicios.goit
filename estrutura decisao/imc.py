peso = float(input("Digite o seu peso:  "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

if imc <= 18.5:
    print("Abaixo do peso")
if imc > 18.5 > 25:
    print("Peso ideal")
if imc > 25 > 30:
    print("Sobrepeso")
if imc > 30 > 40:
    print("Obesidade")
if imc > 40:
    print("Obseidade mórbida")