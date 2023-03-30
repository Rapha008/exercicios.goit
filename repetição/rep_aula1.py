print("Programa para ler 10 nº, somar e calcular a média!")
soma = 0
i = 0
#quanto for preciso o usuario digitar o limite utilizar o código a baixo ou excluir ele e não esquecer de verificar o while a qtd digitada
qtdNum = int(input("Quantos números você deseja somar? "))
while i <= qtdNum:   # <= substituir pela quantidade de vezes que o laço vai rodar
    print("Digite o", i, "número")
    n = float(input())
    soma = soma +n
    i = i + 1


media = soma /qtdNum   #não esqueça de alterar os valores
print("A soma = ", soma)
print("A média é = ", media)
