import os, sys

# Limpar o terminal
os.system("cls")

# Usar acentuação sem bugs - UTF-8
sys.getfilesystemencoding() 

# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
# https://wiki.python.org.br/ExerciciosListas

lista_numeros = []

while len(lista_numeros) < 5:
    numeros = input("Informe 5 números: ")
    lista_numeros.append(numeros)

for numero in lista_numeros:
    print(numero)
    
print(lista_numeros)

# ARQUIVO MODIFICADO







