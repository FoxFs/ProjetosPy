from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = ()
for k, v in jogo.items():
    print(f"o {k} tirou {v}")
    sleep(1)
print("-=-" * 10)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, c in enumerate(ranking):
    print(f"{i}° Lugar: {c[0]} tirou {c[1]} no dado")