def calcular_diferenca(lista):
    # Verifica se a lista está vazia. 
    if not lista: 
        return None
    
# Encontra o maior e o menor elemento da lista.
    maior = max(lista)
    menor = min(lista)

    # Calcula a diferença entre o maior e o menor elemento. 
    diferenca = maior - menor

    return diferenca

# Exemplo de uso
VALORES = [27,15,17,7,2]

resultado = calcular_diferenca(VALORES)

print("A diferença do maior e do menor é:", resultado)





