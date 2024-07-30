numeros = list()
i = list()
for p in range(0, 3):
    n = int(input(f"Digite um Valor para a posição [0,{p}]: "))
    i.append(n)
    numeros.append(i[:])
    i.clear()

for p in range(0, 3): 
    n = int(input(f"Digite um Valor para a posição [1,{p}]: "))
    i.append(n)
    numeros.append(i[:])
    i.clear()

for p in range(0, 3):
    n = int(input(f"Digite um Valor para a posição [2,{p}]: "))
    i.append(n)
    numeros.append(i[:])
    i.clear()

print("Os numeros foram:")
print(f'''
{numeros[0]} {numeros[1]} {numeros[2]}
{numeros[3]} {numeros[4]} {numeros[5]}
{numeros[6]} {numeros[7]} {numeros[8]}''')