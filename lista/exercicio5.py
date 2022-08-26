import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.
# https://wiki.python.org.br/ExerciciosListas

lista_numeros = []
lista_numeros_pares = []
lista_numeros_impares = []

while len(lista_numeros) < 20:
    numeros = input("Informe 20 números inteiros: ")
    lista_numeros.append(int(numeros))
print()
for numero in lista_numeros:
    if int(numero) % 2 == 0:
        lista_numeros_pares.append(numero)
    else:
        lista_numeros_impares.append(numero)

print(f'Lista números informados: {lista_numeros}')
print()
print(f'Lista números pares: {lista_numeros_pares}')
print()
print(f'Lista números ímpares: {lista_numeros_impares}')
# for par in lista_numeros_pares:
#     print(par)

# for impar in lista_numeros_impares:
#     print(impar)





