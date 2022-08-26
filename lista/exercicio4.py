import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista_caracteres = []
lista_vogais = ['a', 'e', 'i', 'o', 'u']
lista_consoantes_encontradas = []

while len(lista_caracteres) < 10:
    caracteres = input('Informe 10 caractéres: ')
    lista_caracteres.append(caracteres)

for letra_encontrada in lista_caracteres:
    #in exibe a quantidade de consoantes
    if letra_encontrada not in lista_vogais:
        lista_consoantes_encontradas.append(letra_encontrada)

qtd_consoantes = len(lista_consoantes_encontradas)
print(f'\nForam encontradas {qtd_consoantes} consoante(s)\n') 

for consoante in lista_consoantes_encontradas:
    print(consoante)


