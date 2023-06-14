cliente = input("Digite seu nome:  ")
documento = int(input("Digite número do seu documento: "))

print("              ")
print("------TABELA DE VALORES ---------")
print("carro popular - R$ 90,00 + km percorrido")
print("carro luxo - R$ 150,00 + km percorrido")
print("              ")
print("Qual carro você alugou?")
carro = input("Digite 1 para carro de luxo ou 2 para popular  ")

if carro == 1:
dias = input("Quantos dias você utilizou o carro? ")
print("O valor da diária ficou em R$: ", dias*90)
