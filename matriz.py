#1)Faça uma matriz que imprime contagem de 1 até 25
"""
# Definindo as dimensões da matriz
linhas = 5
colunas = 5

matriz = [[0] * colunas for _ in range(linhas)]

# Preenchendo a matriz com os números de 1 a 25
contador = 1
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = contador
        contador += 1

# Imprimindo a matriz
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end="\t")
    print()

#1)Faça uma matriz que imprime contagem de 1 até 25
l1 = list(range(26))
print(l1)

#Faça uma matriz que imprime apenas números impares de 1 ate 100

listaimpar = list(range(1,100,2))
print(listaimpar)

#Faça uma matriz que imprime a tabuada do 9, mas não imprima o 0.
tabuada9 = list(range(9,90,9))
print(tabuada9)


#)Faça uma matriz que imprime a tabuada que o usuário queria
numero = int(input("Digite um número para a tabuada: "))

# Definir o tamanho da matriz
linhas = 10
colunas = 2

# Criar a matriz preenchida com zeros
matriz = [[0] * colunas for _ in range(linhas)]

# Preencher a matriz com a tabuada do número escolhido
for i in range(linhas):
    matriz[i][0] = numero
    matriz[i][1] = (i + 1) * numero

# Imprimir a matriz
for i in range(linhas):
    print(f"{matriz[i][0]} x {i+1} = {matriz[i][1]}")


#Faça uma matriz 5x5 que imprima os números pares, e números impares você coloca X
linha = 5
coluna = 5

matriz = [[0] * coluna for _ in range(linha)]

for i in range(linha):
    for p in range(coluna):
        if (i * coluna + p + 1) % 2 == 0:
            matriz[i][p] = i * coluna + p + 1 
        else:
            matriz[i][p] = 'E'

for i in range (linha):
    for p in range(coluna):
        print (matriz[i][p], end='\t')
    print
"""

#Faça uma matriz 5x5 que imprima de A até E Como o exemplo abaixo:
# Definindo as dimensões da matriz
# Definir as dimensões da matriz
linhas = 5
colunas = 5

matriz = [[0] * colunas for _ in range(linhas)] # Criar a matriz preenchida com zeros

# Preencher a matriz com as letras de A até E
for i in range(linhas): 
    letra = chr(65 + i)  # Converte o código  ESSE CÓDIGO FOI ENCONTRADO NA INTERNTWEASCII para letra maiúscula
    for j in range(colunas):
        matriz[i][j] = letra

# Imprimir a matriz
for i in range(linhas):
    print(matriz[i])