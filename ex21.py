#separamento de numeros por listas pares e impares
impar = []
par = []

n = int(input("Digite um numero: "))
#se o numero for divisivel por 2 e sobrar nada(0) ele retorna o comando de enviar o mesmo para a lista par
if n % 2 == 0:
    par.append(n)
else:
    impar.append(n)

answer = str(input("Deseja cadastrar mais algum numero[S/N]? "))
while answer not in "Nn":
    n = int(input("Digite mais um numero: "))
    #se o numero for divisivel por 2 e sobrar nada(0) ele retorna o comando de enviar o mesmo para a lista par
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    answer = str(input("Deseja cadastrar mais algum numero[S/N]? "))

print(f"A lista de numeros pares foram: {par}")
print(f"A lista de numeros impares foram: {impar}")
#lista completa com todos os numeros adicionando o "+" para isso
all = par+impar
print(f"Lista completa: {all}")