from random import choice

selecoes = {
    'commebol': ['Equador', 'Uruguai', 'Peru'],
    'concacaf': ['Canadá', 'México', 'Estados Unidos'],
    'europa': ['Dinamarca', 'Alemanha', 'Sérvia', 'Portugal', 'Suiça', 'Holanda', 'Polônia', 'País de Gales'],
    'africa': ['Senegal', 'Camarões', 'Marrocos', 'Tunísia', 'Gana'],
    'asia': ['Irã', 'Coreia do Sul', 'Japão', 'Arábia Saudita', 'Austrália']
}
cabeças_de_chave = {'cabeças' : ['Brasil', 'Argentina', 'Qatar', 'França', 'Espanha', 'Inglaterra', 'Bélgica', 'Croácia']}

lista = []
grupo_A = []
grupo_B = []
grupo_C = []
grupo_D = []
grupo_E = []
grupo_F = []
grupo_G = []
grupo_H = []
resultado = 0
cont = 0

for c in range(0, 100):
    sor = choice(cabeças_de_chave['cabeças'])
    if sor in lista:
        del sor
        continue
    else:
        lista.append(sor)
        cont += 1
        if cont == 1:
            grupo_A.append(sor)
        elif cont == 2:
            grupo_B.append(sor)
        elif cont == 3:
            grupo_C.append(sor)
        elif cont == 4:
            grupo_D.append(sor)
        elif cont == 5:
            grupo_E.append(sor)
        elif cont == 6:
            grupo_F.append(sor)
        elif cont == 7:
            grupo_G.append(sor)
        else:
            grupo_H.append(sor)
    resultado = sor

cont_1 = 0
lista_total = []
for i in range(1, 9):
    cont_1 += 1
    if cont_1 == 1:
        sorteio_africa = choice(selecoes['africa'])
        sorteio_asia = choice(selecoes['asia'])
        sorteio_europa = choice(selecoes['europa'])
        if sorteio_africa in grupo_A:
            del sorteio_africa
        elif sorteio_asia in grupo_A:
            del sorteio_asia
        elif sorteio_europa in grupo_A:
            del sorteio_europa
        grupo_A.append(sorteio_africa)
        grupo_A.append(sorteio_asia)
        grupo_A.append(sorteio_europa)
        print()
        print('Grupo A')
        for h in grupo_A:
            print(h)
    elif cont_1 == 2:
        sorteio_concacaf = choice(selecoes['concacaf'])
        sorteio_asia = choice(selecoes['asia'])
        sorteio_europa = choice(selecoes['europa'])
        if sorteio_concacaf in grupo_B:
            del sorteio_concacaf
        elif sorteio_asia in grupo_B:
            del sorteio_asia
        elif sorteio_europa in grupo_C:
            del sorteio_europa
        grupo_B.append(sorteio_africa)
        grupo_B.append(sorteio_asia)
        grupo_B.append(sorteio_europa)
        print()
        print('Grupo B')
        for h in grupo_B:
            print(h)
    elif cont_1 == 3:
        sorteio_africa = choice(selecoes['africa'])
        sorteio_concacaf = choice(selecoes['concacaf'])
        sorteio_europa = choice(selecoes['europa'])
        if sorteio_africa in grupo_C:
            del sorteio_africa
        elif sorteio_concacaf in grupo_C:
            del sorteio_concacaf
        elif sorteio_europa in grupo_C:
            del sorteio_europa
        grupo_C.append(sorteio_africa)
        grupo_C.append(sorteio_concacaf)
        grupo_C.append(sorteio_europa)
        print()
        print('Grupo C')
        for h in grupo_C:
            print(h)
    if cont_1 == 4:
        sorteio_america = choice(selecoes['commebol'])
        sorteio_asia = choice(selecoes['asia'])
        sorteio_europa = choice(selecoes['europa'])
        if sorteio_america in grupo_D:
            del sorteio_america
        elif sorteio_asia in grupo_D:
            del sorteio_asia
        elif sorteio_europa in grupo_E:
            del sorteio_europa
        grupo_D.append(sorteio_america)
        grupo_D.append(sorteio_asia)
        grupo_D.append(sorteio_europa)
        print()
        print('Grupo D')
        for h in grupo_D:
            print(h)
    if cont_1 == 5:
        sorteio_africa = choice(selecoes['africa'])
        sorteio_asia = choice(selecoes['asia'])
        sorteio_europa = choice(selecoes['europa'])
        if sorteio_africa in grupo_E:
            del sorteio_africa
        elif sorteio_asia in grupo_E:
            del sorteio_asia
        elif sorteio_europa in grupo_E:
            del sorteio_europa
        grupo_E.append(sorteio_africa)
        grupo_E.append(sorteio_asia)
        grupo_E.append(sorteio_europa)
        print()
        print('Grupo E')
        for h in grupo_E:
            print(h)
    if cont_1 == 6:
        sorteio_africa = choice(selecoes['africa'])
        sorteio_america = choice(selecoes['commebol'])
        sorteio_europa = choice(selecoes['europa'])
        if sorteio_africa in grupo_F:
            del sorteio_africa
        elif sorteio_america in grupo_F:
            del sorteio_america
        elif sorteio_europa in grupo_F:
            del sorteio_europa
        grupo_F.append(sorteio_africa)
        grupo_F.append(sorteio_america)
        grupo_F.append(sorteio_europa)
        print()
        print('Grupo F')
        for h in grupo_F:
            print(h)
    if cont_1 == 7:
        sorteio_america = choice(selecoes['commebol'])
        sorteio_asia = choice(selecoes['asia'])
        sorteio_europa = choice(selecoes['europa'])
        if sorteio_america in grupo_G:
            del sorteio_america
        elif sorteio_asia in grupo_G:
            del sorteio_asia
        elif sorteio_europa in grupo_G:
            del sorteio_europa
        grupo_G.append(sorteio_america)
        grupo_G.append(sorteio_asia)
        grupo_G.append(sorteio_europa)
        print()
        print('Grupo G')
        for h in grupo_G:
            print(h)
    if cont_1 == 8:
        sorteio_africa = choice(selecoes['africa'])
        sorteio_concacaf = choice(selecoes['concacaf'])
        sorteio_europa = choice(selecoes['europa'])
        if sorteio_africa in grupo_H:
            del sorteio_africa
        elif sorteio_concacaf in grupo_H:
            del sorteio_concacaf
        elif sorteio_europa in grupo_H:
            del sorteio_europa
        grupo_H.append(sorteio_africa)
        grupo_H.append(sorteio_concacaf)
        grupo_H.append(sorteio_europa)
        print()
        print('Grupo H')
        for h in grupo_H:
            print(h)

