from random import randint
cont = 0
while True:
    valor = randint(1, 10)
    try:
        tentativa = int(input('Advinhe de 1 a 10:'))
        acertou = 0 
        if tentativa == valor:
            acertou += 1
            print(f'Parabéns você acertou. O número da máquina foi: {valor}')
        else:
            print('Você errou')
        
        cont += 1
        if cont == 5:
            cont = 0
            p = str(input('Deseja continuar ? [S/N] ')).upper().strip()
            if p == 'N':
                break
            while p not in 'SN':
                p = str(input('Deseja continuar ? [S/N] ')).upper().strip()
    except ValueError:
        print('Ocorreu um erro. Informe um valor correto')

print(f'Você acertou: {acertou}')
