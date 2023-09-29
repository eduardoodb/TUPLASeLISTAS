def a(lista):
    menor = lista[0]
    b = 0

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            b = i

    return menor, b

numeros = []

quantidade = int(input("Digite os números da lista: "))

for i in range(quantidade):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

c, indice = a(numeros)

print("O menor elemento da lista é:", c)
print("Sua posição (índice) na lista é:", indice)