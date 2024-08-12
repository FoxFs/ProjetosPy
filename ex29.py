#um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres e homens D) Uma lista de pessoas com idade acima da média. #

pessoa = {}
grupo = []
allage = []
qtdpesso = 0

print(" ")
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade: "))
    allage.append(idade)
    pessoa['Idade'] = idade
    while True:
        pessoa['Sexo'] = str(input("Sexo[M/F]: ")).strip().upper()[0]
        if pessoa['Sexo'] in "MF":
            break
        print("ERRO!, tente novamente  e apenas digite M ou F")
    qtdpesso += 1
    grupo.append(pessoa.copy())
    while True:
        op = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
        if op in "SN":
            break
        print("Erro! apenas digite S ou N")
    if op in "Nn":
        break
print("-=" * 15)
media = sum(allage) / qtdpesso
print(f"A) {qtdpesso} pessooas foram cadastradas!")
print(f"B) A media de idades foi {media}")

print("-=" * 15)
print("C) A lista de todas mulheres foi", end=" ")
for p in grupo:
    if p['Sexo'] in 'F':
        print(f"{p['Nome']}", end=",")
print()
print("C) A lista de todos homens foi", end=" ")
for p in grupo:
    if p['Sexo'] in "M":
        print(f"{p['Nome']}", end=", ")
print()
print("D) Nome das pessoas acima da média:", end=" ")
for p in grupo:
    if p['Idade'] > media:
        print(f"{p['Nome']}", end=", ")