# Selection Sort -> Parte do princípio de que a lista não está ordenada

def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Principal
lista = [-2, 40, 30, 0, -5, 50, 32, -222, 90, 2]
print(f'Lista: {lista}')
print('Odenando a lista...')
selection_sort(lista)
print(f'Lista ordenada: {lista}')