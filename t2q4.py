def soma_cumulativa(lista):
    saida = []
    for i in range(len(lista)):
        if i == 0:
            saida.append(lista[i])
        else:
            saida.append(saida[i-1] + lista [i])


    return saida

def main():
    entradas = []
    while True:
        entrada = int(input())
        if entrada == 0: break
        entradas.append(entrada)

    novaLista = soma_cumulativa(entradas)

    print(novaLista)

if __name__ == '__main__':
    main()