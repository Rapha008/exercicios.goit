dist = float(input("Digite a distância que você irá percorrer:  "))

if dist <= 200:
    print ("Sua corrida ficará em R$: ", dist * 0.50)

elif dist > 200:
    print("Sua corrida ficará em R$:  ", dist * 0.45)