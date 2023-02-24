import math
print("A fórmula da distância entre dois pontos no plano cartesiano é d(x,y) = raiz(x2 - x1)² + (y2 + y1)²")
x1 = int(input("digite a coordenada xa: "))
y1 = int(input("digite a coordenada ya: "))
x2 = int(input("digite a coordenada xb: "))
y2 = int(input("digite a coordenada yb: "))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if d >= 10:
    print("longe")
else:
    print("perto")

print(d)


