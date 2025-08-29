# Minha solução

def contar_na_lista(lista):
    tamanho_lista = 0
    if lista == []:
        return 0
    else:
        tamanho_lista = contar_na_lista(lista[1:])
    return tamanho_lista + 1

print(contar_na_lista([1, 2, 3, 4, 5, 1, 2, 3]))  # Saída: 8

# solução do livro

def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:])

print(conta([1, 2, 3, 4, 5, 1, 2, 3]))  # Saída: 8