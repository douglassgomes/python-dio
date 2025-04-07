# Exibe o menu
menu = """
===== OPÇÕES =====

[D] Depositar
[S] Sacar
[E] Exibir Extrato
[F] Finalizar

=>"""

saldo = 0
extrato = ""
numero_saques = 0

# Função para realizar depósitos
def depositar():
    global saldo
    global extrato

    # Tratamento de erro caso o valor informado não seja número
    while True:
        try:
            valor = float(input("Informe o valor do depósito: "))
            break
        except ValueError:
            print("Erro! Por favor, digite apenas números, substituindo a vírgula por ponto, se for o caso.\n")

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação não realizada! O valor informado é inválido!")

# Função para realizar saques
def sacar():
    global saldo
    global extrato
    global numero_saques

    limite = 500
    LIMITE_SAQUES = 3

    # Tratamento de erro caso o valor informado não seja número
    while True:
        try:
            valor = float(input("Informe o valor do saque: "))
            break
        except ValueError:
            print("Erro! Por favor, digite apenas números, substituindo a vírgula por ponto, se for o caso.\n")

    # variáveis para verificação das condições de saque
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação não realizada! Conta não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação não realizada! Valor do saque excedeu o limite.")

    elif excedeu_saques:
        print("Operação não realizada! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    
    else:
        print("Operação não realizada! O valor informado é inválido!")

# Função para exibir o extrato
def exibe_extrato():
    global saldo
    global extrato

    print("\n============== EXTRATO ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=====================================")

# Tratamento de opções do menu
while True:
    opcao = input(menu)

    # Converte a letra digitada para minúscula para evitar erro na comparação
    opcao_tratada = opcao.lower()

    if opcao_tratada == "d":
        depositar()
    elif opcao_tratada == "s":
        sacar()
    elif opcao_tratada == "e":
        exibe_extrato()
    elif opcao_tratada == "f":
        print("Obrigado por ser nosso(a) cliente!\n")
        break
    else:
        print("Operação inválida! Por favor, selecione corretamente a opção desejada.")









