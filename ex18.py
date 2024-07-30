palavras = ("gato", "cachorro", "pássaro", "peixe", "elefante", "tigre", "leão", "girafa", "macaco", "cavalo", "urso", "coelho", "rato", "tartaruga", "raposa")

for palavra in palavras:
    print(f"\n a palavra {palavra.upper()} possui as vogais:", end=" ")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra , end=" ")