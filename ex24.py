import time
nf = []
allu = []
np = []

while True:
    allu.append(str(input("Digite o nome do aluno: ").capitalize()))
    nota = float(input("Digite a 1° nota: "))
    nota2 = float(input("Digite a 2° nota: "))
    media = nota + nota2
    np.append(nota)
    np.append(nota2)
    allu.append(np[:])
    nf.append(allu[:])
    allu.clear()
    np.clear()
    pergunta = input("Quer continuar[S/N]? ")
    if pergunta in "Nn":
        break

print("No.  NOME                MÉDIA")
print("___" * 15)
for n, a in enumerate(nf):
    print(f"{n}   {a[0] :<10}      {sum(a[1])/2 :>10}")
print("---" * 15)
while True:
    op = int(input("quer ver as notas de qual aluno? (999 interrompe): "))
    if op <= len(nf):
        print("___" * 15)
        print("No.  NOME                NOTAS")
        print(f"{op}  {nf[op][0]}   {nf[op][1]}")
    elif op == 999:
        print("DESLIGANDO PROGRAMA.")
        time.sleep(1.5)
        print("DESLIGANDO PROGRAMA..")
        time.sleep(1)
        print("DESLIGANDO PROGRAMA...")
        time.sleep(0.5)
        print("<<<Volte Sempre>>>")
        break