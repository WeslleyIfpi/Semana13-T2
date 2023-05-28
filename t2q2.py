def multiplicaLista(lista):
    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i] = lista[i] * 3
        else:
            lista[i] = lista[i] * 5
    
    return lista


def main():
    entradas = []
    for i in range(100):
        entradas.append(int(input()))
    
    listaOrdenada = sorted(entradas)

    listaOrdMultiplicada = multiplicaLista(listaOrdenada)

    print(listaOrdMultiplicada)


if __name__ == '__main__':
    main()