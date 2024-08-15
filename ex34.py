from random import randint

numeros = list() # Lista inicial

def sorteio(lista): # Função que vai gerar varios numeros e colocar dentro da lista
    for c in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
    print(f"Os numeros sorteados foram: {lista}")

def SomaPar(lista): # Função que vai desempacotar toda lista e somar as variaveis de dentro
    somar = 0
    for n in lista:
        if n % 2 == 0: 
            somar = somar + n
    print(f"A soma dos numeros PARES foi: {somar}")

print("=-=" * 12)
sorteio(numeros) # chamando a função com direito a troca da lista (OBS: se quiser trocar vai ter que modificar a lista inicial)
SomaPar(numeros) # chamando a função com direito a troca da lista (OBS: se quiser trocar vai ter que modificar a lista inicial)
print("=-=" * 12)