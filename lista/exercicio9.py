import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 9 - Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.
# https://wiki.python.org.br/ExerciciosListas

lista_soma_quadrados = []
soma_quadrados = 0

for i in range(10):
    print('Número {}: '.format(i+1))
    numeros = input()
    lista_soma_quadrados.append(int(numeros))

for numero in lista_soma_quadrados:
    soma_quadrados += (numero * numero) 

print("A soma dos quadrados do Vetor A é {}".format(soma_quadrados))







