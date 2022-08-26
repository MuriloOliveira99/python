import os, sys

os.system("cls")
sys.getfilesystemencoding() 

# 11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
# https://wiki.python.org.br/ExerciciosListas

lista_a = []
lista_b = []
lista_c = []
lista_d = []


for _ in range(10):
    valor_a = int(input("Lista A: "))
    lista_a.append(valor_a)

for _ in range(10):
    valor_b = int(input("Lista B: "))
    lista_b.append(valor_b)

for _ in range(10):
    valor_c = int(input("Lista C: "))
    lista_c.append(valor_c)

for z in range(10):
    lista_d.append(lista_a[z])
    lista_d.append(lista_b[z])
    lista_d.append(lista_c[z])
    
print(lista_d)


