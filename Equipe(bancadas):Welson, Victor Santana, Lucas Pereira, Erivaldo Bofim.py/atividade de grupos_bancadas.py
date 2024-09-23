import os
import time

# FUNÇÕES
def limpa_tela():
    os.system("cls || clear")

def verificando_pares_impares(lista_numeros):
    contador_par = 0
    contador_impar = 0
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            contador_par += 1
            pares.append(numero)
        else:
            contador_impar += 1
            impares.append(numero)

    return contador_par, contador_impar, pares, impares

def verificando_positivos_negativos(lista_numeros):
    contador_positivo = 0
    contador_negativo = 0
    for numero in lista_numeros:
        if numero > 0:
            contador_positivo += 1
        elif numero < 0:
            contador_negativo += 1

    return contador_positivo, contador_negativo

def processando_maior_menor(lista_numeros):
    maior = max(lista_numeros)
    menor = min(lista_numeros)

    return maior, menor

def processando_medias(pares, impares, lista_numeros):
    media_pares = sum(pares) / len(pares)
    media_impares = sum(impares) / len(impares) 
    media_geral = sum(lista_numeros) / len(lista_numeros)

    return media_pares, media_impares, media_geral

# ENTRADA
limpa_tela()
lista_numeros = []
quantidade_numeros = 5

for i in range(quantidade_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)
    limpa_tela()

# PROCESSAMENTO:

#PARES E ÍMPARES
contador_pares, contador_impares, pares, impares = verificando_pares_impares(lista_numeros)
#POSITIVOS E NEGATIVOS
contador_positivos, contador_negativos = verificando_positivos_negativos(lista_numeros)
# MAIOR E MENOR
maior_numero, menor_numero = processando_maior_menor(lista_numeros)
# MÉDIA
media_pares, media_impares, media_geral = processando_medias(pares, impares, lista_numeros)

# SAÍDA 
limpa_tela()
time.sleep(0.5)
print(f"A quantidade de números digitados: {len(lista_numeros)}")
time.sleep(0.5)
for i,numero in enumerate(lista_numeros):
    print(f"O {i+1}º:{numero} ")
time.sleep(0.5)
print(f"Quantidade de pares: {contador_pares}")
time.sleep(0.5)
print(f"Quantidade de ímpares: {contador_impares}")
time.sleep(0.5)
print(f"Quantidade de positivos: {contador_positivos}")
time.sleep(0.5)
print(f"Quantidade de negativos: {contador_negativos}")
time.sleep(0.5)
print(f"Maior número: {maior_numero}")
time.sleep(0.5)
print(f"Menor número: {menor_numero}")
time.sleep(0.5)
print(f"Média dos números pares: {media_pares:.2f}")
time.sleep(0.5)
print(f"Média dos números ímpares: {media_impares:.2f}")
time.sleep(0.5)
print(f"Média de todos os números: {media_geral:.2f}")
time.sleep(0.5)
print("\nNúmeros na ordem inversa:")
for numero in reversed(lista_numeros):
    print(numero)
    time.sleep(0.5)