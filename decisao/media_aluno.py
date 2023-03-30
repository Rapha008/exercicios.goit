print ("Relatório Escolar - Go-iT - ")
print (input("Digite seu nome:  "))
print (input("Digite seu curso:  "))
print("---------------------------")
nota1 = float(input("Digite sua 1º nota:  "))
nota2 = float(input("Digite sua 2ª nota:  "))
nota3 = float(input("Digite sua 3ª nota:  "))

notas = nota1+nota2+nota3
media = notas/3

if media >= 7:
    print("Você está aprovado, sua média foi de:  ", media  ,"Parabéns e boas Férias!")

else:
    media 
    print("Você está de recuperação, Infelizmente as recuperações começam na próxima semana!")
