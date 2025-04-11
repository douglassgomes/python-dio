from datetime import datetime

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
numero_operacoes_dia = 0
LIMITE_OPERACOES_DIA = 10
data_atual = datetime.now().date()

# Função para verificar e atualizar a data para fins de controle de operações diárias
def verificar_data():
    global numero_operacoes_dia
    global numero_saques
    global data_atual

    hoje = datetime.now().date()

    if hoje != data_atual:
        numero_operacoes_dia = 0
        numero_saques = 0
        data_atual = hoje
        print(f"\nIniciando novo dia... Contadores de operações reiniciados!")
        print(f"\nLembrando que você pode realizar até {LIMITE_OPERACOES_DIA} operações por dia.")

# Função para realizar depósitos
def depositar():
    global saldo
    global extrato
    global numero_operacoes_dia
    data_hora = datetime.now()
    data = data_hora.strftime("%d/%m/%Y")
    hora = data_hora.strftime("%H:%M")

    verificar_data()

    # Verifica se excedeu o limite de operações diárias
    excedeu_operacoes_dia = numero_operacoes_dia >= LIMITE_OPERACOES_DIA

    if excedeu_operacoes_dia:
        print(f"Operação não realizada! Você excedeu o limite de {LIMITE_OPERACOES_DIA} operações no dia de hoje.")
        return

    # Tratamento de erro caso o valor informado não seja número
    while True:
        try:
            valor = float(input("Informe o valor do depósito: "))
            break
        except ValueError:
            print("Erro! Por favor, digite apenas números, substituindo a vírgula por ponto, se for o caso.\n")  

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} => Realizado em {data}, às {hora}.\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        numero_operacoes_dia += 1
    else:
        print("Operação não realizada! O valor informado é inválido!")

# Função para realizar saques
def sacar():
    global saldo
    global extrato
    global numero_saques
    global numero_operacoes_dia
    data_hora = datetime.now()
    data = data_hora.strftime("%d/%m/%Y")
    hora = data_hora.strftime("%H:%M")
    limite = 500
    LIMITE_SAQUES = 3

    verificar_data()

    # Verifica se excedeu o limite de operações diárias
    excedeu_operacoes_dia = numero_operacoes_dia >= LIMITE_OPERACOES_DIA
    
    if excedeu_operacoes_dia:
        print(f"Operação não realizada! Você excedeu o limite de {LIMITE_OPERACOES_DIA} operações no dia de hoje.")
        return
    
    # Tratamento de erro caso o valor informado não seja número
    while True:
        try:
            valor = float(input("Informe o valor do saque: "))
            break
        except ValueError:
            print("Erro! Por favor, digite apenas números, substituindo a vírgula por ponto, se for o caso.\n")
    
    # Variáveis para verificação das demais condições de saque
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
        extrato += f"Saque: R$ {valor:.2f} => Realizado em {data}, às {hora}.\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        numero_saques += 1
        numero_operacoes_dia += 1
        
    else:
        print("Operação não realizada! O valor informado é inválido!")

# Função para exibir o extrato
def exibe_extrato():
    global numero_operacoes_dia
    data_hora = datetime.now()
    data = data_hora.strftime("%d/%m/%Y")
    hora = data_hora.strftime("%H:%M")

    verificar_data()

    excedeu_operacoes_dia = numero_operacoes_dia >= LIMITE_OPERACOES_DIA

    if excedeu_operacoes_dia:
        print(f"Operação não realizada! Você excedeu o limite de {LIMITE_OPERACOES_DIA} operações no dia de hoje.")
        return

    print("\n========================= EXTRATO =========================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f} em {data}, às {hora}.")
    print(f"Quantidade de operações diárias: {numero_operacoes_dia}")
    print("===========================================================")
    numero_operacoes_dia += 1
    
# Tratamento de opções do menu
while True:
    verificar_data()    
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









