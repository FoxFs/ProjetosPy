import time

def contador(init, fim, passo):
    if init < fim:
        print("CONTAGEM: ", end="")
        for n in range(init, fim + 1 , passo):
            print(f"{n}", end=" ", flush=True)
            time.sleep(1)
        print("FIM!")

    else:
        print("CONTAGEM: ", end="")
        for n in range(init, fim - 1 , - passo):
            print(f"{n}", end=" ", flush=True)
            time.sleep(1)
        print("FIM!")


print("Bem Vindo ao contador!")
print("==" * 10)
initperg = int(input("Inicio da contagem: "))
fimperg = int(input("Fim da contagem: "))
passoperg = int(input("Passo: "))
print("==" * 10)

contador(initperg, fimperg, passoperg)