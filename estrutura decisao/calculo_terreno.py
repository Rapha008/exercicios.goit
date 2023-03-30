largura = float(input("Digite a largura:   "))
h = float(input("Digite o cumprimento:  "))

area = largura*h

if area <= 100:
    print("ESTE TERRENO É POPULAR e sua area é igual a:  ", area)

if area > 100 <= 500:
    print("ESTE TERRENO É MASTER e sua area é igual a:  ", area)

else: 
    area > 500
    print("ESTE TERRENO É VIP e sua area é igual a:  ", area)