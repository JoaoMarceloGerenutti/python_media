''' =======================================
ESAMC -  Faculdade de Sorocaba
Programa usando FOR
Disciplina 	: Lógica de Programação e Algoritmos
Professor	: Francisco Tesifom Munhoz
Data	: 1º semestre de 2020
===========================================
Atividade	: Exercício 04.1
Autor	: João Marcelo Gerenutti
Data	: 31/05/2020
Comentários	: "Faça um programa que leia 10 números digitados pelo usuário (utilizando um laço for). No final, calcule a média dos números fornecidos."
============================================
'''

# DECLARAÇÂO DE VARIAVEL
soma = 0
num_posicao = 1
num_1 = int
num_2 = int
media = float

# SAIDA DE DADOS
print("---------------------------------------------")

# ENTRADA DE DADOS
for item in range(0, 10):

    # SAIDA DE DADOS
    print("Digite o", num_posicao, "º número")

    # PROCESSAMENTO DE DADOS
    num_posicao = num_posicao + 1

    # ENTRADA DE DADOS
    num = int(input("---> "))

    # PROCESSAMENTO DE DADOS
    num_1 = soma
    soma = soma + num
    num_2 = num

    # SAIDA DE DADOS
    print("A soma de", num_1, "+", num_2, "é: ", soma)
    print("---------------------------------------------")

# PROCESSAMENTO DE DADOS
media = (soma / 10)

# SAIDA DE DADOS
print("A média dos 10 números é: %.1f" % media)
print("---------------------------------------------")