print("Calculadora de ano Bissexto ")
ano = int(input("Digite um ano:  "))

if (ano % 4 == 0) and (ano % 100 != 0):
    print ("o ano", ano, "é Bissexto")

elif (ano % 100 == 0) and (ano % 400 == 0):
    print("o ano", ano, "é Bissexto")

else:
    print("Não, este ano não é Bissexto!  ")