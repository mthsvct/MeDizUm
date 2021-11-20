from medizum import Medizum

diz = Medizum()

'''
print('Sorteio de nomes de cidades do Piauí')
for i in range(50):
	print(f'{diz.cidade(cod_uf="PI")}')
'''


'''
print('Sorteio de CPFs:')
for i in range(15):
	print(f'{i}: \t{diz.cpf()}')
'''


print('Sorteio de cores: ')
for i in range(10):
	print(f'{i}: \t{diz.cor(hexadecimal=True)}')
