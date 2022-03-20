from random import randint

dado = {}
dado_1 = []
while True:
	try:
		jogo = int(input('Quantos jogos você quer jogar ?'))
		for c in range(1, jogo + 1):
			dado.clear()
			dado['valores'] = randint(1, 6)
			print(dado)
			dado_1.append(dado.copy())

	except ValueError:
		print('Ocorreu um erro. Escreva o valor adequado')
	
	p = str(input('Deseja continuar ? [S/N] ')).upper().strip()
	if p == 'N':
		break
	while p not in 'SN':
		p = str(input('Deseja continuar ? [S/N] ')).upper().strip()

print(dado_1)
