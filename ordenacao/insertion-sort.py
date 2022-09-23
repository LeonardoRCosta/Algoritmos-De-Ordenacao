# Ordenação por inserção

def insertion_sort(lista):
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i - 1 # índice do elemento anterior
        while j >= 0 and pivo < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = pivo

# Principal
lista = [5, 2, 4, 6, 1, 3]
print("Lista original: ", lista)
insertion_sort(lista)
print("Lista ordenada: ", lista)