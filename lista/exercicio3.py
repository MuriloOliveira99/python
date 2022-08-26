import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista_notas = []
media = 0

while len(lista_notas) < 4:
    notas = input("Informe as 4 notas: ")
    lista_notas.append(float(notas))

    media = sum(lista_notas) / len(lista_notas)

print(media)

