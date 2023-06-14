"""
n=int(input('Digite um numero:  '))

if(n==10):
    print('numero digitado é 10')

elif (n<10):
    print('Numero é menor que 10')

else:
    print('Numero é maior que 10')

salario=float(input('Digite seu atual salario:  '))

if (salario<500):
    nvSal=salario*1.15
    print('Seu salario teve um reajuste de 15%% e seu novo salário será: ', nvSal)

elif (salario<=1000):
    nvSal=salario*1.05
    print('Seu salario teve um reajuste de 10%% eseu novo salário será: ', nvSal)

else:
    nvSal=salario*1.10
    print('Seu salario teve um reajuste de 5%% e seu novo salario é: ', nvSal)
"""
n='012345 678'

print (n[0])
print (n[7])
print (n[:5])
print (n[3:])
print (n[0])