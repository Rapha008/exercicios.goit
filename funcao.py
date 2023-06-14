# Crie um programa que tenha uma função Gerador () que, quando chamado,
#mostre a mensagem EX:"Olá, Mundo!" com algum componente visual (linhas)
#Ex: Ao chamar Gerador() aparece:
#+-------=======------+
#Olá, Mundo!
#+-------=======------+
"""
def Gerador():
    print('+-------=======------+',end="\t")
    print('       Olá mundo      ',end="\t")
    print('+-------=======------+',end="\t")

Gerador()

 Crie um programa que tenha uma função Media (), que vai receber as 2 notas
de um aluno e retornar a sua média para o programa principal.


def media(nota1, nota2):
    return (nota1 + nota2) /2

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

resultado = media(nota1, nota2)
print("A média do aluno é:", resultado)
"""

def maior(valor1, valor2, valor3):
    if valor1 >= valor2 and valor1 >= valor3:
        return valor1
    elif valor2 >= valor1 and valor2 >= valor3:
        return valor2
    else:
        return valor3
    
valor1 = float(input("Digite o primeiro número: ").replace(",", "."))
valor2 = float(input("Digite o segundo número: ").replace(",", "."))
valor3 = float(input("Digite o terceiro número: ").replace(",", "."))

nmmaior = maior(valor1, valor2, valor3)
print("O maior número é:", nmmaior)
