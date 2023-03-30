anonas = int(input("Digite seu ano de nascimento:  "))

calc = 2022 - anonas

if calc > 18:
    print("Você já passou,",calc - 18, "anos da data de alistamento")

else:
    print("você precisa se alistar em: ", 18 - calc, "anos")

