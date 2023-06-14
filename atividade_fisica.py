cliente = input("Digite seu nome:  ")
hrs = float(input("Quantos aulas você veio neste mês?   "))


if hrs <= 10:
    calc = hrs*2
    print("você fez ", calc,"e ganhou", calc*0.05, "em bônus")
if hrs > 10 < 20:
    calc = hrs*5
    print("você fez ", calc,"e ganhou", calc*0.05, "em bônus")
if hrs >= 20:
    calc = hrs*10
    print("você fez ", calc,"e ganhou", calc*0.05, "em bônus")