#!/usr/bin/python3
# -*- coding: utf -8-*

import sys
import csv
import calcoohija

calculadora = calcoohija.CalculadoraHija()

with open(sys.argv[1], newline = '') as fich:
    lineas = csv.reader(fich)
    for linea in lineas:           

        op1 = int(linea[1])
        op2 = int(linea[2])

        if linea[0] == 'suma':
            resultado = calculadora.suma(op1, op2)
           
        elif linea[0] == 'resta':
            resultado = calculadora.resta(op1, op2)
       
        elif linea[0] == 'divide':
            resultado = calculadora.div(op1, op2)

        elif linea[0] == 'multiplica':
            resultado = calculadora.mult(op1, op2)
                    
        for elem in linea[3:]:
               
            if linea[0] == 'suma':
                resultado = calculadora.suma(resultado,int(elem))
                                 
            elif linea[0] == 'resta':
                resultado = calculadora.resta(resultado, int(elem))
                    
            elif linea[0] == 'divide':
                resultado = calculadora.div(resultado, int(elem))
                    
            elif linea[0] == 'multiplica':
                resultado = calculadora.mult(resultado, int(elem))
            
        print(resultado)
