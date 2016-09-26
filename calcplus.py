#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoohija
import sys

fich = open(sys.argv[1], 'r')
lineas = fich.readlines()

if __name__ == '__main__':

	calculadora = calcoohija.CalculadoraHija()
	for linea in lineas:

		elems = linea[:-1].split(',')
		
		op1 = int(elems[1])
		op2 = int(elems[2])

		if elems[0] == 'suma':
			resultado = calculadora.suma(op1, op2)
		elif elems[0] == 'resta':
			resultado = calculadora.resta(op1, op2)
		elif elems[0] == 'divide':
			resultado = calculadora.div(op1, op2)
		elif elems[0] == 'multiplica':
			resultado = calculadora.mult(op1, op2)

		for elem in elems[3:]:

			if elems[0] == 'suma':
				resultado = calculadora.suma(resultado, int(elem))
			elif elems[0] == 'resta':
				resultado = calculadora.resta(resultado, int(elem))
			elif elems[0] == 'divide':
				resultado = calculadora.div(resultado, int(elem))
			elif elems[0] == 'multiplica':
				resultado = calculadora.mult(resultado, int(elem))

		print(resultado)
