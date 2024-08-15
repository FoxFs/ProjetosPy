from random import randint
import time

quantidades = list()
for c in range(0, 6):
    num = randint(0, 50)
    while True:
        if num not in quantidades:
            quantidades.append(num)
            break
        else:   
            num = randint(0, 15)
            quantidades.append(num)
            break

def maior(*numbers):
    maior = 0
    for item in numbers:
        if item > maior:
            maior = item
    print(f"O maior numero é: {maior}")

print("=-=" * 12)
print("Analisando os valores passados..")
time.sleep(1)
print(f"A lista completa de numeros é {quantidades} com o total de {len(quantidades)} numeros")
time.sleep(1)
maior(*quantidades)
print("=-=" * 12)