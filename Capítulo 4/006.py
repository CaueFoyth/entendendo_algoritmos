def quicksort(array):
    if len(array) < 2:
        return array # Base: arrays com 0 ou 1 elemento já estão "ordenados".
    else:
        pivo = array[0] # Caso recursivo
        menores = [i for i in array[1:] if i <= pivo] # Subarray de todos os elementos menores do que o pivô.
        maiores = [i for i in array[1:] if i > pivo] # Subarray de todos os elementos maiores do que o pivô.
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
print(quicksort([10, 5, 2, 3]))  # Saída: [2, 3, 5, 10]