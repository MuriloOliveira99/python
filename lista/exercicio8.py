import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 8 - Faça um Programa que peça a idade e a altura de 5 pessoas, 
# armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.
# https://wiki.python.org.br/ExerciciosListas

lista_idades = []
lista_alturas = []

#Gerar uma idade e uma altura para 5 pessoas
for _ in range(1, 6):
    print('Pessoa {}'.format(_))
    idade = int(input('Sua idade: '))
    altura = float(input('Sua altura: '))
    print()
    lista_idades.append(idade)
    lista_alturas.append(altura)

print('####### ORDEM LIDA #######')
print(f'Idades: {lista_idades}')
print('Alturas: {}'.format(lista_alturas))

print('\n####### ORDEM INVERSA #######')

print(f'Idades Inversa: {lista_idades[::-1]}')
print('Alturas Inversa: {} '.format(lista_alturas[::-1]))
