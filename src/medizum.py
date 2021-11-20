import pandas as pd
from random import randint, uniform

class Medizum():

	def __init__(self):
		self.nomes_masc = pd.read_csv('dados/nomes_masculinos.csv')
		self.nomes_fem = pd.read_csv('dados/nomes_femininos.csv')
		self.cidades = pd.read_csv('dados/cidades.csv')
		self.paises = pd.read_csv('dados/paises.csv')

	def sorteia(self, arq):
		i = randint(0, len(arq)-1)
		retorno = arq.loc[i][0]
		return retorno


	def nome(self, qnt=1, sexo=None, sobrenome=True):
		if sexo == None:

			return self.nome( qnt=qnt, sexo=self.sexo(), sobrenome=sobrenome )

		else:

			nomes = []

			while(qnt > 0):

				if sexo == 'M':
					n = self.sorteia(self.nomes_masc)
				else:
					n = self.sorteia(self.nomes_fem)


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


	def peso(self, qnt=1, minimo=30.0, maximo=120.0):
		p = []
		while qnt > 0:
			p.append( round( uniform(minimo, maximo), 2 ) )
			qnt -= 1
		if len(p) == 1:
			peso = p[0]
		else:
			peso = p
		return peso


