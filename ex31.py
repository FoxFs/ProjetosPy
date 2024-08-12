#faça uma programa que tenha uma função chamada ESCREVA, que receba um texto como paramentro e mostre uma mensagem com tamanho adaptavel
def escreva(txt):
    print("*" * len(txt))
    print(txt)
    print("*" * len(txt))


texto = str(input("Escreva um texto: "))
escreva(texto)