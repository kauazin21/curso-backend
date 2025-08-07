def busca(indice, item, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1

    if inicio <= fim:
        meio = (inicio + fim) // 2

        if indice[meio] == item:
            return meio
        
        if item < indice[meio]:
            return busca(indice, item, inicio, meio - 1)
        
        else:
            return busca(indice, item, meio + 1, fim)
        
    return None
        
lista = [11, 24, 27, 30, 50, 77, 99]
itens = [24, 50, 35]
resultados = []

for item in itens:
    posicao = busca(lista, item)
    resultados.append((item, posicao))


print(f"Os itens {itens} vão ser procurados na lista {lista}.")

for item, posicao in resultados:
    if posicao is not None:
        print(f"O item {item} foi encontrado na posição {posicao}")
    else:
        print(f"Item {item} não encontrado")
