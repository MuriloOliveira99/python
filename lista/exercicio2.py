import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista_numeros = []

while len(lista_numeros) < 10:
    numeros = input("informe 10 números: ")
    lista_numeros.append(numeros)

print(lista_numeros)
lista_numeros.reverse()
print(lista_numeros)

for numero in lista_numeros:
    print(numero)
