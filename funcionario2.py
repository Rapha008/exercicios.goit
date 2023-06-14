print (input("Qual seu nome? "))
sexo = int(input("Digite 1 para MASCULINO ou 2 para FEMININO: "))
tempo = int(input("Digite quantos anos você traalha nesta empresa: "))
salario = float(input("Digite seu atual salário: "))

if sexo==2:
    if tempo <= 15:
        salnov=salario*0.05
    if tempo < 15 ==20:
        salnov=salario*0.12
    if tempo >=20:
        salnov=salario*0.23
    
if sexo==1:
    if tempo <= 20:
        salnov=salario*0.03
    if tempo < 20 ==30:
        salnov=salario*0.13
    if tempo >=30:
        salnov=salario*0.25

valor = salario+salnov

print("O seu novo salário será de: ", valor)