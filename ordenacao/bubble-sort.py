def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i] # Atribuição paralela

def empurra(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            troca(lista, i, i + 1)

def bubble_sort(lista):
    t = len(lista)
    while t > 1:
        empurra(lista)
        t -= 1

# Principal
lista = [40, 30, 20, 50, 10]
bubble_sort(lista)
print(lista)