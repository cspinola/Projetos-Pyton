lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

for index in range(0, len(lista)):
    # Maior	valor
    if(maiorValor < lista[index]):
        maiorValor = lista[index]
    # Menor	valor
    if(menorValor > lista[index]):
        menorValor = lista[index]
        # Numeros	pares
        if(lista[index] % 2 == 0):
            listaPares.append(lista[index])
        # Numero	de	ocorrências
        if(lista[index] == lista[0]):
            ocorrenciasItem1 = ocorrenciasItem1 + 1
        # Soma	dos	números	negativos
        if(lista[index] < 0):
            somaNegativos = somaNegativos + lista[index]
