import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 6 - Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.
# https://wiki.python.org.br/ExerciciosListas


lista_alunos = []
lista_notas = []

for aluno in range(4):
    print(f'Aluno {aluno+1}:')

    for _ in range(2):
        nota = input("Nota: ")
        lista_notas.append(nota)

    lista_alunos.append(lista_notas)
    lista_notas = []

print(lista_alunos)