#um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média. #

pessoa = {}
grupo = []
allage = []
qtdpesso = 0

while True:
    pessoa['Nome'] = str(input("Nome: ").strip().capitalize())
    idade = int(input("Idade: "))
    pessoa['Idade'] = idade
    pessoa['Sexo'] = str(input("Sexo: ").strip().capitalize())
    op = str(input("Quer continuar? [S/N]: ").strip().capitalize())

    if op in "Ss":
        grupo.append(pessoa.copy())
        qtdpesso += 1
        pass

    elif op in "Nn":
        break

    else:
        print("Pedido invalido!, Tente Novamente")

print(f"{qtdpesso} pessooas foram cadastradas!")
print(f"A media de idades foi {sum(idade) / qtdpesso}")

#more