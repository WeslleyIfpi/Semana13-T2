def multiplica_constante(lista, CONST):
    saida = []
    for i in range(len(lista)):
        saida.append(lista[i]*CONST)
    
    return saida

def main():
    entradas = []
    while True:
        entrada = int(input())
        if entrada == 0: break
        entradas.append(entrada)

    CONST = int(input())
    novaLista = multiplica_constante(entradas, CONST)

    print(novaLista)

if __name__ == '__main__':
    main()