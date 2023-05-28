def media6(notas):
    aprovados = []
    for i in range(len(notas)):
        if notas[i] >= 6:
            aprovados.append(i)

    return aprovados

def main():
    entradas = []
    for i in range(50):
        entradas.append(float(input()))

    aprovados = media6(entradas)

    print(aprovados)

if __name__ == '__main__':
    main()