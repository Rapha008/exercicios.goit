''''
senha = "2408"
leitura = input('Digite a senha: ')

while (leitura!= senha):
        print('Senha Incorreta. Tente Novamente')
        leitura=input('Dgite a senha: ')

print('Acesso Liberado')
'''''
'''''
senha = "2408"
leitura = input('Digite a senha: ')

while (leitura!= senha):
    if leitura == senha:
       print('Acesso Liberado! ') 
    else:
        print('Senha Incorreta. Tente Novamente')
    leitura=input('Dgite a senha: ')
else:
    print('Acesso Liberado')
    '''''

senha = "2408"
leitura = int(input('Digite a senha: '))
if leitura >= 1000 and leitura <= 9999:
    while (leitura!= senha):
        print('Senha Incorreta. Tente Novamente')
        leitura=input('Dgite a senha: ')
else:
    leitura=input
print('Acesso Liberado')