import pandas as pd
from random import randint, uniform

class Medizum():

	def __init__(self):
		self.nomes_masc = pd.read_csv('dados/nomes_masculinos.csv')
		self.nomes_fem = pd.read_csv('dados/nomes_femininos.csv')
		self.cidades = pd.read_csv('dados/cidades.csv')
		self.estados = pd.read_csv('dados/estados.csv')
		self.paises = pd.read_csv('dados/paises.csv')


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








