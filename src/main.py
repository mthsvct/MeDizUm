from medizum import Medizum

diz = Medizum()

print('Sorteio de nomes de cidades do Piauí')
for i in range(50):
	print(f'{diz.cidade(cod_uf="PI")}')