import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# https://wiki.python.org.br/ExerciciosListas

lista_a = []
lista_b = []
lista_c = []

for i in range(10):
    numero = input("Lista A: ")
    lista_a.append(numero)
for i in range(10):
    numero = input("Lista B: ")
    lista_b.append(numero)

for z in range(10):
    lista_c.append(lista_a[z])
    lista_c.append(lista_b[z])

print(lista_a)
print(lista_b)
print(lista_c)

