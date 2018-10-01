#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 09:19:14 2018

@author: cvillar
"""

import sys


class calculadora():

    def plus(self, op1, op2):
        """ Function to sum the operands. Ops have to be ints """
        return op1 + op2

    def minus(self, op1, op2):
        """ Function to substract the operands """
        return op1 - op2


class calculadoraHija(calculadora):

    def multi(self, op1, op2):
        """Función para multiplicar los operandos"""
        return op1 * op2

    def division(self, op1, op2):
        """Función para dividir los operandos"""
        return op1 / op2


if __name__ == "__main__":

    mi_calc = calculadoraHija()

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
            result = mi_calc.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
            result = mi_calc.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
            result = mi_calc.multi(operando1, operando2)
    elif sys.argv[2] == "divide":
            if operando2 == 0:
                sys.exit("Error:Division by zero is not allowed")
            else:
                result = mi_calc.division(operando1, operando2)
    else:
        sys.exit("Operación sólo puede ser sumar,restar,multiplicar o dividir")

    print(result)
