#print ("Digite 7 valores inteiros")
soma = 0
vl = 1
par = 0
impar = 0
while vl<=3:
    print("Digite o valor", vl)
    n = int(input())
    if n % 2 == 0:
        par=par+1
    else:
        impar=impar+1
    vl=vl+1
print('par', par)
print('impar ', impar)

#print("A soma dos inteiros é: ", soma)
