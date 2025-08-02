import math
import sys


def calculos(numero1,operacao,numero2):
    if operacao == '+':
        resultado = numero1+numero2
    elif operacao== "-":
        resultado = numero1-numero2
    elif operacao == "*":
            resultado = numero1*numero2
    elif operacao == "/":
        try:
            resultado = numero1/numero2
        except ZeroDivisionError:
            print("não é possivel dividir por zero")

    print("-"*50)
    print("RESULTADO :",resultado)
    print("-"*50)


print("-"*50)
print("BEM VINDO A CALCULADORA")
print("-"*50)
 
numero1 = int(input('escreva o numero 1: '))
print("-"*50)
operacao = input('escrava a operação (+, -, *, /): ')
print("-"*50)
numero2 = int(input('escreva o numero 2: '))


calculos(numero1,operacao,numero2)
