def buscaMenor(arr):
    menor = arr[0] # Armazena o menor valor
    menor_indice = 0 # Armazena o índice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr): # Ordenação em um array
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) # Encontra o menor elemento do array e adiciona ao novo array
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))  # Saída: [2, 3, 5, 6, 10]