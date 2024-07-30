#DESAFIO: um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = list()

print('-=-' * 15)
jogador['nome'] = str(input("Nome do jogador: ").strip().capitalize())
print(f"Quantas partidas {jogador['nome']} jogou? ")
for c in range(0, 5):
    gol = int(input(f"Quantos gols ele fez na partida {c}: "))
    gols.append(gol)
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=-' * 15)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")
print('-=-' * 15)
print(f'O jogador {jogador["nome"]} jogou 5 partidas')
for p in range(0, 5):
    print(f" => Na partida {p}, fez {gols[p]} gols")
print(f"fazendo um total de {jogador['total']}")