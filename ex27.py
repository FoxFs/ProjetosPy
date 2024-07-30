#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.#

#variaveis
import datetime as dt
pessoa = {}
muie = 62
homi = 65
ano_atual = dt.date.today().year

pessoa['nome'] = str(input("Digite o nome da pessoa: ")).strip().capitalize()
nascimento = int(input("Digite o ano do seu nascimento: "))
idade = ano_atual - nascimento
pessoa['idade'] = idade
pessoa['sexo'] = str(input("Qual o seu sexo?[M/F]: ")).strip().capitalize()
if pessoa['sexo'] not in "MF":
    print("Erro!! sintaxe de gênero não identificada")
else:
    pessoa['ctps'] = int(input("Digite a sua CTPS (caso não tenha digite 0): "))
    if pessoa['ctps'] == 0:
        print("bocó")
    else:
        pessoa['ano_contratação'] = int(input("Qual o ano de contratação: "))
        pessoa['salario'] = float(input("Salário: R$"))
        if pessoa["sexo"] in "M":
            pessoa['aposentadoria'] = homi - idade
        elif pessoa["sexo"] in "F":
            pessoa["aposentadoria"] = muie - idade
    
print("=-=" * 10)
for k, v in pessoa.items():
    print(f"o item [{k}] tem valor: {v}")