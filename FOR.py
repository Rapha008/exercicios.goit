"""
#Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem: 0 5 10 15 20 25 30 35 40 Acabou!

for i in range(0,45,5):
    print(i, end= " ")

print("Acabou")

#Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem: 100 90 80 70 60 50 40 30 20 10 0 Acabou!

for i in range(100,-1,-10):
    print(i, end=" ")

print ("ACABOU")

numero=int(input('Digite um valor para taboada: '))

for i in range (1,11):
    resultado=numero*i
    print (f'{numero} x {i} = {resultado}')

# Criar um vetor numérico com 8 posições
vetor = [123] * 8

# Imprimir o vetor
for i in range(len(vetor)):
    print(vetor[i], end="\t")

# Imprimir as posições
print("\n", end="")
for i in range(len(vetor)):
    print(i, end="\t")
"""
# Criar um vetor numérico com 10 posições
vetor = [0] * 20

# Preencher o vetor com os valores sequenciais
valor = 5
for i in range(len(vetor)):
    vetor[i] = valor
    valor += 5

# Imprimir o vetor
for i in range(len(vetor)):
    print(vetor[i], end="\t")

# Imprimir as posições
print("\n", end="")
for i in range(len(vetor)):
    print(i, end="\t")
