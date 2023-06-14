print("Qual carro você alugou? ")
escarro=int(input("Digite 1 para carro popular ou 2 para carro de luxo: "))
diaria=int(input("Digite quantos dias você utilizou o carro: "))
km=int(input("digite quantos kilometros você rodou ex.100: "))
if escarro==1:
    carro=90
    if km<=100:
        valkm=km*0.20
    if km>100:
        valkm=km*0.10
    
if escarro==2:
    carro=150
    if km<=200:
        valkm=km*0.30
    if km>200:
        valkm=km*0.25

valor=carro*diaria
total=valor+valkm
print("O valor a pagar em diaria's', será de ",valor," e o de km rodado's',",valkm," total,",total)