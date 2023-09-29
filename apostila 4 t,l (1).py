def par(xy):
    soma = 0
    
n = []
xy = []
resultado = 0

for c in range(4):
    n.append(int(input(f"Digite um numero qualquer: ")))

    for c in n:
        if c % 2 == 0:
            xy.append(c)

    for c in xy:
        resultado += c


resultado = par(xy)

print("A soma dos números par são:", resultado)
