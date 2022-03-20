lista = ['Entrou na floresta', 'Está passando pelo vale', 'A estrada está próxima', 'Logo aparecerão os animais',
'Olhe para o céu e você encontrará o caminho', 'A sua casa está mais próxima do que você imagina', 
'Você chegou em casa, Descanse. Amanhã é outro dia', 
'Parabéns, você saiu da floresta']

while True:
    try:
        caminho = int(input('Digite o número do caminho: '))
        if caminho == 0:
            print(lista[0])
        elif caminho == 1:
            print(lista[1])
        elif caminho == 2:
            print(lista[2])
        elif caminho == 3:
            print(lista[3])
        elif caminho == 4:
            print(lista[4])
        elif caminho == 5:
            print(lista[5])
        elif caminho == 6:
            print(lista[6])
        elif caminho == 7:
            print(lista[7])
            break
    except ValueError:
        print('Valor incorreto')   
    