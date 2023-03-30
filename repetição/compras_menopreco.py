#"aplicativo que leia o preço de 8 produtos"
soma = maior = menor = 0
i = 1
#qtitens = int(input("Quantos itens você deseja comprar? "))

while i <= 5:   
    print("Digite o valor da compra", i)
    n = float(input())
    soma = soma +n

    i = i+1 
    if n == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n 

print('O maior valor foi: ', maior, ' e o menor valor foi: ', menor)


