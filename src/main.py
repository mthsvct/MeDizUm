from medizum import Medizum
from PIL import Image
import os
from threading import Thread


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


'''
print('Sorteio de cores: ')
for i in range(10):
	print(f'{i}: \t{diz.cor(rgb=True)}')
'''


'''
print('Sorteio de imagens com cores diferentes: ')
for i in range(10):
	imagem = diz.imagem()
	imagem.save("imagem"+str(i)+".png")
	os.system("xdg-open imagem"+str(i)+".png")
'''


'''
print('Sorteio de idades:')
for i in range(3):
	print(diz.idade(5, minimo=18))
	print(diz.idade(crianca=True),'anos.')
	print(diz.idade(adolescente=True),'anos.')
	print(diz.idade(adulto=True),'anos.')
	print(diz.idade(idoso=True),'anos.')
	print('-' * 15)
'''


'''
print('Sorteio de alturas: ')
for i in range(3):
	print(diz.altura(),'m')
	print(diz.altura(minimo=1.5),'m')
	print(diz.altura(3))
'''


'''
print('Sorteio de emails:')
for i in range(3):
	print(diz.email())
	print(diz.email(nome='jorge'))
	print(diz.email(3))
	print('-'*15)
'''

'''
print('Sorteio de um arquivo: ')
diz.arquivo()
'''

'''
print('Sorteio de dias: ')
for i in range(3):
	print(f'0 - {diz.dia()}')
	print(f'1 - {diz.dia(fds=False)}')
	print(f'2 - {diz.dia(util=False)}')
	print(f'3 - {diz.dia(3)}')
	print('-'*15)
'''

print('Sorteio de meses: ')
for i in range(3):
	print(f'{diz.mes()}')
	print(f'{diz.mes(3)}')
	print('-'*15)


