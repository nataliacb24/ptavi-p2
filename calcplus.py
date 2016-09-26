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

        operaciones = {'suma': calculadora.suma, 'resta': calculadora.resta,
                       'divide': calculadora.div, 'multiplica': calculadora.mult}

        operando = elems[0]
        resultado = operaciones[operando](op1, op2)

        for elem in elems[3:]:

            resultado = operaciones[operando](resultado, int(elem))

        print(resultado)
