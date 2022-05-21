dic = {}

while True:
    perg = str(input('Deseja fazer um comentário ? [S/N] ')).strip().upper()[0]
    if perg == 'S':
        dic['coment'] = str(input('Qual o seu comentário ? ')).strip().upper()
        print('Obrigado pelo seu comentário')
    elif perg == 'N':
        print('Até mais !')
        break
    else:
        print('Resposta incorreta')


while True:
    try:
        perg_1 = str(input('Deseja avaliar em estrelas ? [S/N]')).upper().strip()[0]
        while True:
            if perg_1 == 'S':
                try:
                    dic['estrelas'] = int(input('Quantas estrelas você avalia para o nosso serviço ? [0 - 5]'))
                    if dic['estrelas'] <= 5:
                        print('Muito obrigado pela sua resposta !')
                        break
                    else:
                        print('Resposta Incorreta')
                except (ValueError, IndexError):
                    print('Resposta Incorreta')
            elif perg_1 == 'N':
                print('Até mais !')
                break
            else:
                print('Resposta Incorreta')
        break
    except (ValueError, IndexError):
        print('Resposta Incorreta')
