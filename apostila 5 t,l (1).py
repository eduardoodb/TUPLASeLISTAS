def trocar_elementos(lista1, lista2):
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            temp = lista1[i]
            lista1[i] = lista2[i]
            lista2[i] = temp
    else:
        print("As listas devem ter o mesmo número de elementos.")

lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

print("Listas antes da troca:")
print("Lista A:", lista_a)
print("Lista B:", lista_b)

trocar_elementos(lista_a, lista_b)

print("\nListas após a troca:")
print("Lista A:", lista_a)
print("Lista B:", lista_b)