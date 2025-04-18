from datetime import datetime

# Função para exibir o menu
def exibir_menu():
    menu = """
    ====== OPÇÕES ======

    [D]  Depositar
    [S]  Sacar
    [E]  Exibir Extrato
    [IC] Incluir Cliente
    [CC] Cadastar Conta
    [F]  Finalizar

    =>"""

    return input(menu)

# Função para verificar e atualizar a data para fins de controle de operações diárias
def verificar_data(numero_operacoes_dia, numero_saques, data_atual, LIMITE_OPERACOES_DIA):

    hoje = datetime.now().date()

    if hoje != data_atual:
        numero_operacoes_dia = 0
        numero_saques = 0
        data_atual = hoje
        print(f"\nIniciando novo dia... Contadores de operações reiniciados!")
        print(f"\nLembrando que você pode realizar até {LIMITE_OPERACOES_DIA} operações por dia.")
        return numero_operacoes_dia, numero_saques, data_atual
    return numero_operacoes_dia, numero_saques, data_atual

# Função para verificar se excedeu o limite de operações diárias
def verificar_limite_operacoes_dia(numero_operacoes_dia, LIMITE_OPERACOES_DIA):
    if numero_operacoes_dia >= LIMITE_OPERACOES_DIA:
        print(f"Operação não realizada! Você excedeu o limite de {LIMITE_OPERACOES_DIA} operações no dia de hoje.")
        return True
    return False
    
# Função para obter valores numéricos
def obter_valor(mensagem):
    while True:
            try:
                valor = float(input(mensagem))
                if valor <= 0:
                    print("Erro! O valor deve ser maior que zero.")
                    continue
                return valor
            except ValueError:
                print("Erro! Por favor, digite apenas números, substituindo a vírgula por ponto, se for o caso.\n")

# Função para realizar depósitos
def depositar(saldo, extrato, numero_operacoes_dia, LIMITE_OPERACOES_DIA, /):
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M")
    
    if verificar_limite_operacoes_dia(numero_operacoes_dia, LIMITE_OPERACOES_DIA):
        return saldo, extrato, numero_operacoes_dia
    
    else:
        valor = obter_valor("Informe o valor do depósito: ")
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} => Realizado em {data}, às {hora}.\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        numero_operacoes_dia += 1

    return saldo, extrato, numero_operacoes_dia

# Função para realizar saques
def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES, numero_operacoes_dia, LIMITE_OPERACOES_DIA):
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M")

    if verificar_limite_operacoes_dia(numero_operacoes_dia, LIMITE_OPERACOES_DIA):
        return saldo, extrato, numero_saques, numero_operacoes_dia
    
    elif numero_saques >= LIMITE_SAQUES:
        print(f"Operação não realizada! Número máximo de {LIMITE_SAQUES} saques diários excedido.")
        return saldo, extrato, numero_saques, numero_operacoes_dia

    valor = obter_valor("Informe o valor do saque: ")

    if valor > saldo:
        print("Operação não realizada! Conta não tem saldo suficiente.")
        return saldo, extrato, numero_saques, numero_operacoes_dia
    
    elif valor > limite:
        print("Operação não realizada! Valor do saque excedeu o limite.")
        return saldo, extrato, numero_saques, numero_operacoes_dia
    
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} => Realizado em {data}, às {hora}.\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        numero_saques += 1
        numero_operacoes_dia += 1

    return saldo, extrato, numero_saques, numero_operacoes_dia

# Função para exibir o extrato
def exibir_extrato(numero_operacoes_dia, saldo, LIMITE_OPERACOES_DIA, /, *, extrato):
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M")
    
    if verificar_limite_operacoes_dia(numero_operacoes_dia, LIMITE_OPERACOES_DIA):
        return numero_operacoes_dia
    
    else:
        exibe_operacoes = numero_operacoes_dia+1
        print("\n========================= EXTRATO =========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f} em {data}, às {hora}.")
        print(f"Quantidade de operações diárias: {exibe_operacoes}")
        print("===========================================================")
        numero_operacoes_dia += 1

        return numero_operacoes_dia
    
# Função para criação(cadastramento) de clientes
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_clientes(cpf, clientes)
    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    
    clientes.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Cliente cadastrado com sucesso!")

# Função para filtrar clientes
def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Função para criação de conta corrente
def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        numero_conta += 1
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    
    print("\nCliente não encontrado! Não foi possível criar a conta. Verifique o CPF e tente novamente.")
        
# Função principal para tratamento de opções do menu
def main():
    LIMITE_OPERACOES_DIA = 10
    numero_operacoes_dia = 0
    data_atual = datetime.now().date()
    saldo = 0
    extrato = ""
    numero_saques = 0
    limite = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    clientes = []
    contas = []

    while True:
        verificar_data(numero_operacoes_dia, numero_saques, data_atual, LIMITE_OPERACOES_DIA)
        opcao = exibir_menu()

        # Converte a letra digitada para minúscula para evitar erro na comparação
        opcao_tratada = opcao.lower()

        if opcao_tratada == "d":
            saldo, extrato, numero_operacoes_dia = depositar(saldo, extrato, numero_operacoes_dia, LIMITE_OPERACOES_DIA)

        elif opcao_tratada == "s":
            saldo, extrato, numero_saques, numero_operacoes_dia = sacar(
                    saldo = saldo,
                    extrato = extrato,
                    limite = limite,
                    numero_saques = numero_saques,
                    LIMITE_SAQUES = LIMITE_SAQUES,
                    numero_operacoes_dia = numero_operacoes_dia,
                    LIMITE_OPERACOES_DIA = LIMITE_OPERACOES_DIA
                )

        elif opcao_tratada == "e":
            numero_operacoes_dia = exibir_extrato(numero_operacoes_dia, saldo, LIMITE_OPERACOES_DIA, extrato = extrato)

        elif opcao_tratada == "ic":
            criar_cliente(clientes)

        elif opcao_tratada == "cc":
            numero_conta = 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)

        elif opcao_tratada == "f":
            print("Obrigado por ser nosso(a) cliente!\n")
            break

        else:
            print("Operação inválida! Por favor, selecione corretamente a opção desejada.")

main()