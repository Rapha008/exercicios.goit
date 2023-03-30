cliente = (input("Qual seu nome? "))
sexo = int(input("Digite 1 para MASCULINO ou 2 para FEMININO: "))
compras = float(input("Digite o valor de suas compras: "))
#salario = float(input("Digite seu atual salário: "))

calcF = compras*0.13
calcM = compras*0.05

if sexo==2:
    print("Suas compras deram: ", compras, "E com desconto ficou:", compras-calcF)

if sexo==1:
    print("Suas compras deram: ", compras, "E com desconto ficou:", compras-calcM)