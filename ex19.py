numeros = []

resposta = input("Deseja adicionar um numero[S/N]? ")
qtd_de_numero = 0
qtd_num_cinco = 0

if resposta in "Ss":
    while resposta != "Nn":
        #variavel onde vai receber o numero
        numero = int(input("Digite um Numero: "))
        if numero in numeros:
            print("Não posso adicionar numero repetido")
        else:
            if numero == 5:
                qtd_num_cinco += 1
                qtd_de_numero += 1
                numeros.append(numero)
            else:
                qtd_de_numero += 1
                numeros.append(numero)

        resposta = input("Deseja adicionar um numero[S/N]? ")
        if resposta in "Nn":
            print(" " * 10)
            print(f"{qtd_de_numero} numeros foram digitados, sendo eles: {numeros}")
            print(f"Aqui está a lista de forma decrescente: {sorted(numeros, reverse=True)}")
            print(f"o numero cinco foi digitado {qtd_num_cinco} vez(es)")
            print("Tenha um bom dia!")
            break

elif resposta in "Nn":
    print("Tenha um bom dia!")

else:
    print("ERRO!!!")