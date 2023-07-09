import os
from datetime import date


def limpar_tela():
    os.system('clear')

LIMITE_QUANTIDADE_SAQUE = 3
quantidade_saques_realizados = 0
limite_valor_saque = 500
extrato = ""
saldo = 0

x = 0
while True:
    limpar_tela()
    print("Digite o numero correspondente a opção desejada: ")
    print("0. Extrato")
    print("1. Saque")
    print("2. Depósito")
    print("3. Sair")
    x = int(input())

    if x == 3: # Sair
        break

    if x == 0: # Extrato
        print(f"Saldo: R$ {saldo:.2f}")
        print(extrato)
        print("Pressione qualquer tecla para voltar.")
        input()

    if x == 1: # Saque
        if saldo <= 0:
            print("Saldo Insuficiente. Tecle para voltar")
            input()
            continue
        if quantidade_saques_realizados >= LIMITE_QUANTIDADE_SAQUE:
            print("Quantidade de Saques excedidas. Tecle para voltar.")
            input()
        print("Digite o valor do Saque: ")
        valor = float(input())
        data_atual = date.today()
        if valor > saldo:
            print("Saldo insuficiente. Tecle para voltar")
            input()
            continue
        if valor > limite_valor_saque:
            print("Valor limite de R$ 500,00 excedido. Tecle para voltar")
            input()
            continue
        saldo -= valor
        quantidade_saques_realizados += 1
        if extrato is "":
            extrato += f"Saque Realizado. Valor: R$ {valor:.2f}. Data: " + str(data_atual)
        elif extrato is not "":
            extrato += f"\nSaque Realizado. Valor: R$ {valor:.2f}. Data: " + str(data_atual)

    if x == 2: # Depósito
        print("Digite o valor do Depósito: ")
        valor = float(input())
        data_atual = date.today()
        if valor <= 0:
            print("Valor incorreto. Favor digitar um valor acima de 0.")
        saldo += valor
        if extrato is "":
            extrato += f"Depósito Realizado. Valor: R$ {valor:.2f}. Data: " + str(data_atual)
        elif extrato is not "":
            extrato += f"\nDepósito Realizado. Valor: R$ {valor:.2f}. Data: " + str(data_atual)
