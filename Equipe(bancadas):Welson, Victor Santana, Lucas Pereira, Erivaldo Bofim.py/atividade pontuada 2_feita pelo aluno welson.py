"""Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de seus colegas não concluiu. 
O objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela.

1-A quantidade de números pares e ímpares.
2-A quantidade de números positivos e negativos.
3-A quantidade de números inseridos.
4-O maior e o menor número.
5-A média de números pares.
6-A média de números ímpares.
7-A média de todos os números inseridos.
8-Mostrar os números lidos na ordem inversa.
9-Variáveis para armazenar os números"""

import os
os.system("cls || clear")
#funções
def limpa_tela():
    import os
    os.system("cls || clear")
    return os.system("cls || clear")

def verificador_impar_par(lista_numero1):
    quantidade_impares = 0
    soma_impares = 0
    soma_pares = 0
    quantidade_pares = 0
    lista_pares = []
    lista_impar=[]
    for numero1 in lista_numero1:
        if numero1 % 2 == 0:
            quantidade_pares += 1
            soma_pares += numero1
            lista_pares.append(numero1)
        else:
            quantidade_impares += 1
            soma_impares += 1
            lista_impar.append(numero1)
    return quantidade_pares,quantidade_impares

def verificador_media_impar_par(lista_numero1):
    quantidade_impares = 0
    soma_impares = 0
    soma_pares = 0
    quantidade_pares = 0
    for numero1 in lista_numero1:
        if numero1 % 2 == 0:
            quantidade_pares+=1
            soma_pares+=numero1
            media_par=soma_pares/quantidade_pares
        elif numero1 % 2!=0:
            quantidade_impares+=1
            soma_impares+=numero1
            media_impar=soma_impares/quantidade_impares

    return media_par,media_impar

def verificador_negativo(lista_numero1):
    quantidade_negativos = 0
    for numero1 in lista_numero1:
        if numero1<0:
            quantidade_negativos +=1
    return quantidade_negativos

def verificador_positivo(lista_numero1):
    quantidade_positivos = 0
    for numero1 in lista_numero1:
        if numero1>0:
            quantidade_positivos +=1
    return quantidade_positivos

def verificador_maior_menor(lista_numero1):
    menor_numero=min(lista_numero1)
    maior_numero=max(lista_numero1)
    return menor_numero,maior_numero

def verificador_media(lista_numero1):
    soma_geral = 0
    for numero1 in lista_numero1:
        soma_geral = numero1+numero1+numero1+numero1+numero1
        media_geral=soma_geral/QUANTIDADE
        return media_geral

#declaração de variaveis(constantes)
lista_numero1=[]
QUANTIDADE=5
#solicitação
for i in range(QUANTIDADE):
   numero1 = int(input(f"Digite {i+1}º número: "))
   lista_numero1.append(numero1)
   limpa_tela()

# Processando cada números
quantidade_pares,quantidade_impares=verificador_impar_par(lista_numero1)
media_par,media_impar=verificador_media_impar_par(lista_numero1)
quantidade_positivos=verificador_positivo(lista_numero1)
quantidade_negativos=verificador_negativo(lista_numero1)
menor_numero,maior_numero=verificador_maior_menor(lista_numero1)
media_geral =verificador_media(lista_numero1)

# Mostrando números na ordem inversa
numeros_invertidos = [numero1]
limpa_tela()

# Imprimindo as estatísticas

print("\nEstatísticas dos números:")
print(f"A quantidade de numeros digitados:{QUANTIDADE}")
for i, numero in enumerate (lista_numero1):
    print(f"{i+1}º número:{numero}")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_par:}")
print(f"Média dos números ímpares: {media_impar:}")
print(f"Média de todos os números: {media_geral:}")
for numero in reversed(lista_numero1):
        print(f"Números na ordem inversa: {numero}")