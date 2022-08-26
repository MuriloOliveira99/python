import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 7 - Faça um Programa que leia um vetor de 5 números inteiros, 
# mostre a soma, a multiplicação e os números.
# https://wiki.python.org.br/ExerciciosListas

lista_numeros = []
multiplicacao = 1
soma = 0

# for _ in range()
while len(lista_numeros) < 5:
    numeros = input('Informe 5 números: ')
    lista_numeros.append(numeros)

print()
for numero in lista_numeros:
    multiplicacao *= int(numero)
    soma += int(numero)

print('A soma do array é {}'.format(soma))
print(f'A multiplicacao do array é {multiplicacao}')
print('Os números do array são ' + str(lista_numeros))

