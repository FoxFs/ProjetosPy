numeros = []
maior_numero = 0
menor_numero = 0
for c in range(0, 6):
    numeros.append(int(input(f"Digite um numero para a posição {c}: ")))
    if c == 0:
        maior_numero = menor_numero = numeros[c]
    else:
        if numeros[c] > maior_numero:
            maior_numero = numeros[c]
        if numeros[c] < menor_numero:
            menor_numero = numeros[c]
print(f"O 5 numeros digitados estão aqui:{numeros}")
print(f"O maior numero é o {maior_numero} nas posições ", end="")
for i, v in enumerate(numeros):
    if v == maior_numero:
        print(f"{i}...", end=" ")
print()
print(f"O menor numero é o {menor_numero} nas posições ", end="")
for i, v in enumerate(numeros):
    if v == menor_numero:
        print(f"{i}...", end=" ")
print()