aluno = {}
turma = []
while True:
    aluno['nome'] = str(input("Digite o nome do aluno: ").capitalize())
    n1 = float(input("Digite a 1° nota: "))
    n2 = float(input("Digite a 2° nota: "))
    aluno['média'] = (n1 + n2) / 2
    if aluno["média"] > 7.0:
        aluno['situação'] = "Aprovado"
    else:
        aluno['situação'] = "Negado"
    turma.append(aluno.copy())
    op = str(input("Deseja adicionar mais um?[S/N]: "))
    if op in "Nn":
        break

for p in turma:
    print("___" * 10)
    for k, v in p.items():
        print(f"{k} = {v}")