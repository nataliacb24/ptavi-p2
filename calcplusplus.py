#!/usr/bin/python3
# -*- coding: utf -8-*

import sys
import csv
import calcoohija

calculadora = calcoohija.CalculadoraHija()

with open(sys.argv[1], newline='') as fich:
    lineas = csv.reader(fich)
    for linea in lineas:

        op1 = int(linea[1])
        op2 = int(linea[2])

        operaciones = {'suma': calculadora.suma, 'resta': calculadora.resta,
                       'divide': calculadora.div, 'multiplica': calculadora.mult}

        operando = linea[0]
        resultado = operaciones[operando](op1, op2)

        for elem in linea[3:]:

            resultado = operaciones[operando](resultado, int(elem))

        print(resultado)
