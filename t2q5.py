def estaOrdenado(lista):
    listaOrdenada = sorted(lista)

    return True if listaOrdenada == lista else False

def main():
    entradas = []
    qtdEntradas = int(input())
    for i in range(qtdEntradas):
        entradas.append(input().strip())

    if estaOrdenado(entradas):
       print('LISTA ORDENADA')
    else:
       print('LISTA NÃO ORDENADA')


if __name__ == '__main__':
    main()