#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:09:03 2018

@author: cvillar
"""

import sys

from calcoohija import calculadoraHija
if __name__ == "__main__":
    calc = calculadoraHija()
    with open('fichero.csv', 'r') as fich_calcu:
        Lista = fich_calcu.readlines()

    for line in Lista:
        operacion = True
        num = line.split(',')
        num[-1] = num[-1][:-1]
        operans = num[1:]

        if num[0] == "suma":
            op_inic = 0
            for operando in operans:
                op_inic = calc.plus(op_inic, int(operando))

            print("El resultado de la suma es:", op_inic)

        elif num[0] == "resta":

            op_inic = int(operans[0])
            for operando in operans[1:]:
                op_inic = calc.minus(op_inic, int(operando))

            print("El resultado de la resta es:", op_inic)

        elif num[0] == "multiplica":
            op_inic = 1
            for operando in operans:
                op_inic = calc.multi(op_inic, int(operando))

            print("El resultado de la multiplicacion es:", op_inic)

        elif num[0] == "divide":
            op_inic = int(operans[0])

            try:
                    for operando in operans[1:]:
                        op_inic = calc.division(op_inic, int(operando))
                    print("El resultado de la division es:", op_inic)

            except ZeroDivisionError:
                sys.exit("Error: Division by zero is not allowed")

        else:
            operacion = False
            print("Operación no valida")
