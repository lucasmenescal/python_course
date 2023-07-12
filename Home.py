import os
from datetime import date
import platform


def limpar_tela():
    so = platform.system()
    if so == 'Windows':
        os.system('cls')
    elif so == 'Linux':
        os.system('clear')
    else:
        pass


def listar_contas(contas):
    if contas:
        for conta in contas:
            linha = f"Agência:{conta['agencia']} \nC/C:{conta['numero_conta']} \nTitular:{conta['usuario']['nome']}"
            print("*" * 100)
            print(linha)
            input()
    else:
        return print("Nenhuma conta encontrada!")


def nova_conta(agencia, numero_conta, lista_usuarios):
    cpf = int(input("Informe o CPF do usuário: "))
    usuario = valida_cpf(cpf, lista_usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado!")


def novo_usuario(lista_usuarios):
    print("Digite o cpf: ")
    cpf = int(input())
    usuario = valida_cpf(cpf, lista_usuarios)

    if usuario:
        return print("Usuário ja cadastrado!")

    print("Digite o nome do seu usuário: ")
    nome = str(input())

    print("Digite sua data de nascimento: ")
    data_nascimento = str(input())

    print("Digite o seu enderenço: ")
    endereco = str(input())

    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Conta criada com sucesso! Tecle qualquer tecla para voltar ao menu principal!")
    input()


def valida_cpf(cpf, lista_usuarios):
    cpf_existente = [usuario for usuario in lista_usuarios if usuario['cpf'] == cpf]
    return cpf_existente[0] if cpf_existente else None


def sacar(*, saldo, valor, extrato, limite_valor_saque, quantidade_saques_realizados, limite_quantidade_saque):
    if saldo <= 0:
        return print("Saldo Insuficiente. Tecle para voltar")
    if quantidade_saques_realizados >= limite_quantidade_saque:
        return print("Quantidade de Saques excedidas. Tecle para voltar.")
    data_atual = date.today()
    if valor > saldo:
        return print("Saldo insuficiente. Tecle para voltar")
    if valor > limite_valor_saque:
        return print("Valor limite de R$ 500,00 excedido. Tecle para voltar")
    saldo -= valor
    quantidade_saques_realizados += 1
    if extrato is "":
        extrato += f"Saque Realizado. Valor: R$ {valor:.2f}. Data: {str(data_atual)}"
    elif extrato is not "":
        extrato += f"\nSaque Realizado. Valor: R$ {valor:.2f}. Data: {str(data_atual)}"
    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    data_atual = date.today()
    if valor <= 0:
        return print("Valor incorreto. Favor digitar um valor acima de 0.")
    saldo += valor
    if extrato is "":
        extrato += f"Depósito Realizado. Valor: R$ {valor:.2f}. Data: {str(data_atual)}"
    elif extrato is not "":
        extrato += f"\nDepósito Realizado. Valor: R$ {valor:.2f}. Data: {str(data_atual)}"
    return saldo, extrato


def imprimir_extrato(saldo, /, *, extrato):
    print(f"Saldo: R$ {saldo:.2f}")
    print(extrato)
    print("Pressione qualquer tecla para voltar.")
    input()


def menu():
    limpar_tela()
    print("Digite o numero correspondente a opção desejada: ")
    print("0. Extrato")
    print("1. Saque")
    print("2. Depósito")
    print("3. Listar Contas")
    print("4. Novo Usuário")
    print("5. Nova Conta")
    print("9. Sair")
    x = int(input())
    return x


def main():
    AGENCIA = "0001"
    LIMITE_QUANTIDADE_SAQUE = 3
    lista_usuarios = []
    lista_contas = []
    quantidade_saques_realizados = 0
    LIMITE_VALOR_SAQUE = 500
    extrato = ""
    saldo = 0

    x = 0
    while True:
        x = menu()
        if x == 9:  # Sair
            break

        if x == 0:  # Extrato
            imprimir_extrato(saldo, extrato=extrato)

        if x == 1:  # Saque
            print("Digite o valor do Saque: ")
            valor = float(input())
            saldo, extrato = sacar(saldo=saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite_quantidade_saque=LIMITE_QUANTIDADE_SAQUE,
                                   quantidade_saques_realizados=quantidade_saques_realizados,
                                   limite_valor_saque=LIMITE_VALOR_SAQUE)  # type: ignore

        if x == 2:  # Depósito
            print("Digite o valor do Depósito: ")
            valor = float(input())
            saldo, extrato = depositar(saldo, valor, extrato)  # type: ignore

        if x == 3:  # Depósito
            listar_contas(contas=lista_contas)

        if x == 4:  # Novo Usuário
            novo_usuario(lista_usuarios)

        if x == 5:  # Nova Conta
            numero_conta = len(lista_contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, lista_usuarios)

            if conta:
                lista_contas.append(conta)
                print("Conta adicionada!")
                input()


main()
