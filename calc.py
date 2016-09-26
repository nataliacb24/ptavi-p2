#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2

def multiplicar(op1,op2):
    """ Funcion para multiplicar dos operandos """
    return op1 * op2
    
def dividir(op1,op2):
    """Funcion para dividir dos operandos """
    try:
        return op1/op2    
        
    except ZeroDivisionError:
       sys.exit("Error: El divisor no puede ser cero")
    

if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    
    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)
    elif sys.argv[2] == "mult":
        result = multiplicar(operando1, operando2)
    elif sys.argv[2] == "div":
        result = dividir(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, mult o div.')

    print(result)
