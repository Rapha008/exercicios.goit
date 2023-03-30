ca = int(input("Digite a medida do cateto adjascente 'ou lateral esquerda' do triângulo:  "))
co = int(input("Digite a medida do cateto oposto 'ou lateral direita' do triângulo:  "))
ba = int(input("Digite a medida da base para o triângulo:  "))

frm = ca+co+ba

if frm % 3 == 0:
    print("Estas medidas podem formar m triangulo equilatero,  pois todos os lados são iguais")

elif (ca+co % 2 == 0) and (ba %2 != 0):
    print("Estas medidas formam um triangulo isóceles, pois somente dois lados são iguais")

elif (ca+co %2 != 0) and (ba % 2 != 0):
    print("Estas medidas formam um triangulo escaleno, pois nenhum dos lados são iguais")

else:
    print("sei la mano")