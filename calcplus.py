#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoohija
import sys

fich = open('/tmp/git/fichero', 'r')
lineas = fich.readlines()
    

for linea in lineas:

    calculadora = calcoohija.CalculadoraHija()
    
    elems = linea[:-1].split(',')
    
    for elem in elems: 
    
        elem = 
        
        if elems[0] == 'suma':
            resultado = calculadora.suma(int(elems[1]), int(elems[2]))
       
        elif elems[0] == 'resta':
            resultado = calculadora.resta(int(elems[1]),int(elems[2]))
   
        elif elems[0] == 'divide':
            resultado = calculadora.div(int(elems[1]),int(elems[2]))
        
        elif elems[0] == 'multiplica':
            resultado = calculadora.mult(int(elems[1]),int(elems[2]))

    print(resultado)
