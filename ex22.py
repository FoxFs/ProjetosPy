pessoas = []
dado = []
totpessoas = 0
resposta = str(input("Deseja cadastar uma pessoa[S/N]? "))

while resposta not in "Nn":
        dado.append(str(input("NOME: ").strip()))
        dado.append(float(input("PESO(kg): ")))
        if len(pessoas) == 0:
              maiorpeso = menorpeso = dado[1]
        else:
            if dado[1] > maiorpeso:
                 maiorpeso = dado[1]
            if dado[1] < menorpeso:
                 menorpeso = dado[1]
        pessoas.append(dado[:])
        totpessoas += 1
        dado.clear()
        resposta = str(input("Deseja cadastar uma pessoa[S/N]? "))

print("-=-" * 10)
print(f"{totpessoas} Pessoas foram cadastradas")
print(f"O maior peso foi de {maiorpeso:.1f}kg. peso de ", end="")
for p in pessoas: 
     if p[1] == maiorpeso:
          print(f"{p[0]}...", end="")
print()
print(f"O menor peso foi de {menorpeso:.1f}kg. peso de ", end="")
for p in pessoas:
     if p[1] == menorpeso:
          print(f"[{p[0]}]", end=" ")