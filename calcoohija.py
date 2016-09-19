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
     
    except VauleError:
      sys.exit("Parametros no numericos")
      
      
    if sys.argv[2] == "suma":
        resultado = calculadora.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = calculadora.resta(operando1, operando2)
    elif sys.argv[2] == "dividir":
        resultado = calculadora.div(operando1, operando2)
    elif sys.argv[2] == "multiplicar":
        resultado = calculadora.mult(operando1, operando2)
    else:
        sys.exit("Operacion no valida")
        
    print(resultado)
