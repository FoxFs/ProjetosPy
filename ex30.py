def lin():
     print("-" * 20)

def area(l, h):
     a = l * h
     print(f"A area de um terreno {l} x {h} é de {a:.2f}m²")

lin()
print("Calculadora de terrenos")
lin()
l = float(input("Largura (m): "))
h = float(input("Altura (m): "))
print(area(l, h))