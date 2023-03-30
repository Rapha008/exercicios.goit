print (input("Qual seu nome: "))
velocidade = float(input("Digite a sua velocidade: "))

if velocidade >= 80:
    multa = velocidade - 80
    print("Você ultrapassou o limite de velocidade, pagará uma multa de:  ", multa * 5 )


if velocidade < 80:
    multa = velocidade - 80
    print("Você está no limite permitido, Parabéns!")