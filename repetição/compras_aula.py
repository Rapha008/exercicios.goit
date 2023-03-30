maior = 0
menor = 0
i = 0

while i < 8:   
    print("Digite o valor da compra", i)
    n = float(input())

    if n<menor or menor ==0:
        menor= n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    i = i+1  

print('O maior valor foi: ', maior, ' e o menor valor foi: ', menor)
