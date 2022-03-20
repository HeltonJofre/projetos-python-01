from random import choice

lista = ['Não, está um dia chuvoso', 'Sim, está um ótimo dia', 'Sim, Vai fazer Sol', 'Sim, Dia está aberto',
'Não, O transito hoje está tranquilo']

p = str(input('Pergunta: '))
valor = choice(lista)
print(f'{p}')
print(f'{valor}')
