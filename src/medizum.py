import pandas as pd
from PIL import Image
from random import randint, uniform

class Medizum():

	def __init__(self):
		self.nomes_masc = pd.read_csv('dados/nomes_masculinos.csv')
		self.nomes_fem = pd.read_csv('dados/nomes_femininos.csv')
		self.cidades = pd.read_csv('dados/cidades.csv')
		self.estados = pd.read_csv('dados/estados.csv')
		self.paises = pd.read_csv('dados/paises.csv')
		self.cores = pd.read_csv('dados/cores.csv')


	def sorteia(self, arq):
		i = randint(0, len(arq)-1)
		retorno = arq.loc[i]
		return retorno


	def nome(self, qnt=1, sexo=None, sobrenome=True):
		if sexo == None:

			retorno = self.nome( qnt=qnt, sexo=self.sexo(), sobrenome=sobrenome )

		else:

			nomes = []

			while(qnt > 0):

				if sexo == 'M':
					aux = self.sorteia(self.nomes_masc)
				else:
					aux = self.sorteia(self.nomes_fem)

				n = aux[0]

				if sobrenome == False:
					sem_sobre = n.split(' ')
					n = sem_sobre[0]

				nomes.append(n)

				qnt -= 1

			if len(nomes) == 1:
				retorno = nomes[0]
			else:
				retorno = nomes

		return retorno


	def sexo(self, qnt=1):
		lista = []
		
		while qnt > 0:
			i = randint(1,2)
			if i == 1:
				lista.append('M')
			else:
				lista.append('F')
			qnt -= 1
		
		if len(lista) == 1:
			retorno = lista[0]
		else:
			retorno = lista 

		return retorno


	def peso(self, qnt=1, minimo=15.0, maximo=100.0):
		p = []
		while qnt > 0:
			p.append( round( uniform(minimo, maximo), 2 ) )
			qnt -= 1
		if len(p) == 1:
			peso = p[0]
		else:
			peso = p
		return peso


	def pais(self, qnt=1):
		p = []
		while qnt > 0:
			aux = self.sorteia(self.paises)
			pais = aux[3]
			p.append( pais )
			qnt -= 1

		if len(p) == 1:
			retorno = p[0]
		else:
			retorno = p

		return retorno


	def validaUF(self, cod):
		# Retorna True se for válido.
		# Retorna False se não for válido.
		retorno = False
		for i in range( len(self.estados)-1 ):
			if self.estados.loc[i][1] == cod:
				retorno = True
		return retorno


	def estado(self, qnt=1, cod_uf=False):
		lista = []
		while qnt > 0:
			aux = self.sorteia(self.estados)

			if cod_uf == True:
				lista.append([ aux[0], aux[1] ])
			else:
				lista.append(aux[0])
			qnt -= 1
		if len(lista) == 1:
			retorno = lista[0]
		else:
			retorno = lista
		return retorno


	def uf(self, qnt=1):
		lista = []
		while qnt > 0:
			aux = self.sorteia(self.estados)
			lista.append(aux[1])
			qnt -= 1
		if len(lista) == 1:
			retorno = lista[0]
		else:
			retorno = lista
		return retorno


	def cidade(self, qnt=1, cod_uf=None):
		
		lista = []

		while qnt > 0:
			if cod_uf == None:
				aux = self.sorteia(self.cidades)
			else:
				if self.validaUF(cod_uf) == True:
					while True:
						aux = self.sorteia(self.cidades)
						if aux[0] == cod_uf:
							break
				else:
					lista.append('ERRO: CODIGO UF NÃO FOI ENCONTRADO!')
					break

			lista.append(aux[1])
			qnt -= 1
		if len(lista) == 1:
			retorno = lista[0]
		else:
			retorno = lista

		return retorno


	def cpf(self, qnt=1):
		lista = []
		while qnt > 0:
			# 123.456.789-09
			c = ''
			for i in range(14):
				if i in [3, 7]:
					c = c + '.'
				elif i == 11:
					c = c + '-'
				else:
					c = c + str( randint(0,9) )

			lista.append(c)
			qnt -= 1

		if len(lista) == 1:
			retorno = lista[0]
		else:
			retorno = lista

		return retorno


	def cor(self, qnt=1, hexadecimal=False, rgb=False):
		lista = []
		while qnt > 0:
			cor = []

			aux = self.sorteia(self.cores)

			cor.append(aux[0])

			if hexadecimal == True:
				cor.append(aux[1])

			if rgb == True:
				cor.append( (aux[2], aux[3], aux[4]) )

			lista.append(cor)
			qnt -= 1

		if len(lista) == 1:
			if True in [hexadecimal, rgb]:
				retorno = lista[0]
			else:
				retorno = lista[0][0]
		else:
			retorno = lista		

		return retorno


	def buscaCOR(self, cor):
		ini = 0
		fim = len(self.cores) - 1
		trava = 0
		retorno = None
		while ini <= fim and trava == 0:
			
			meio = ini + (fim - ini)//2


			#print( f'self.cores.loc[meio][0].upper() = {self.cores.loc[meio][0].upper()}')
			#print( f'cor.upper() = {cor.upper()} \n' )

			if self.cores.loc[meio][0].upper() == cor.upper():
				aux = self.cores.loc[meio]
				retorno = [ aux[0], (aux[2], aux[3], aux[4]) ]
				trava = 1
			elif self.cores.loc[meio][0].upper() > cor.upper():
				fim = meio - 1
			elif self.cores.loc[meio][0].upper() < cor.upper():
				ini = meio + 1

		return retorno


	def imagem(self, qnt=1, cor=None, rgb=None, largura=500, altura=500):
		lista = []
		while qnt > 0:
			if rgb == None and cor == None:
				aux = self.cor(rgb=True)
				imagem = Image.new( "RGB", (largura, altura), aux[1])

			elif rgb == None and cor != None:
				aux = self.buscaCOR(cor)
				if aux != None:
					imagem = Image.new( "RGB", (largura, altura), aux[1])
				else:
					imagem = Image.new( "RGB", (largura, altura), 0)

			elif rgb != None and cor == None:
				imagem = Image.new( "RGB", (largura, altura), rgb)

			lista.append(imagem)
			qnt -= 1

		if len(lista) == 1:
			retorno = lista[0]
			#retorno.show()
		else:
			retorno = lista

		return retorno


	def idade(self, qnt=1, minimo=1, maximo=80, crianca=False, adolescente=False, adulto=False, idoso=False):
		lista = []
		while qnt > 0:
			if crianca == True:
				lista.append(randint(1, 12))
			elif adolescente == True:
				lista.append(randint(13, 18))
			elif adulto == True:
				lista.append(randint(18, 59))
			elif idoso == True:
				lista.append(randint(60, 100))
			else:
				lista.append(randint(minimo, maximo))
			qnt -= 1

		if len(lista) == 1:
			retorno = lista[0]
		else:
			retorno = lista

		return retorno


	def altura(self, qnt=1, minimo=0.5, maximo=1.90):
		lista = []
		while qnt > 0:
			lista.append( round( uniform(minimo, maximo), 2 ) )
			qnt -= 1

		if len(lista) == 1:
			retorno = lista[0]
		else:
			retorno = lista

		return retorno


	def email(self, qnt=1, nome=''):
		lista = []
		while qnt > 0:

			if nome == '':
				n = self.nome(sobrenome=False)
			else:
				n = nome

			e = (f'{n}{randint(0,9)}{randint(0,9)}{randint(0,9)}')

			i = randint(1,3)

			if i == 1:
				e = e + ('@gmail.com')
			elif i == 2:
				e = e + ('@hotmail.com')
			else:
				e = e + ('@outlook.com')

			lista.append(e)
			qnt -= 1

		if len(lista) == 1:
			retorno = lista[0]
		else:
			retorno = lista

		return retorno
