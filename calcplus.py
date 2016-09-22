#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoohija
import sys

fich = open('/home/alumnos/ncarrill/Escritorio/ptvi/ptavi-p2/fichero', 'r')
lineas = fich.readlines()


if __name__ == "_main_":

    calculadora = calcoohija.CalculadoraHija()
        
    for linea in lineas:
        
        elems = linea[:-1].split(',')
        
        op1 = int(elems[1])
        op2 = int(elems[2])

        if elems[0] == 'suma':
            resultado1 = calculadora.suma(op1, op2)
       
        elif elems[0] == 'resta':
            resultado2 = calculadora.resta(op1, op2)
   
        elif elems[0] == 'divide':
            resultado3 = calculadora.div(op1, op2)

        elif elems[0] == 'multiplica':
            resultado4 = calculadora.mult(op1, op2)
        
        
        for elem in elems[3:]:
        
            if elems[0] == 'suma':
                resultado = calculadora.suma(resultado1, int(elem))
            
            elif elems[0] == 'resta':
                resultado = calculadora.resta(resultado2, int(elem))
            
            elif elems[0] == 'resta':
                resultado = calculadora.div(resutlado3, int(elem))
            
            elif elems[0] == 'multiplica':
                resultado = calculadora.div(resultado4, int(elem))
                
            print(resultado)
            
