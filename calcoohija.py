#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoo
import sys


class CalculadoraHija(calcoo.Calculadora):

    def mult(self, op1, op2):
        return op1 * op2

    def div(self, op1, op2):
        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

if __name__ == "__main__":

    calculadora = CalculadoraHija()

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Parametros no numericos")

    operando = sys.argv[2]
    
    operaciones = {'suma': calculadora.suma, 'resta': calculadora.resta,
                   'divide': calculadora.div, 'multiplica': calculadora.mult}

    resultado = operaciones[operando](operando1, operando2)
    print(resultado)
