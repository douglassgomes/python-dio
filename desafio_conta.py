from datetime import datetime
from abc import ABC, abstractmethod
from typing import List

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: str):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Cliente:
    def __init__(self, pessoa_fisica: PessoaFisica, endereco: str):
        self.endereco = endereco
        self.cpf = pessoa_fisica.cpf
        self.nome = pessoa_fisica.nome
        self.data_nascimento = pessoa_fisica.data_nascimento
        self.contas: List["Conta"] = []
        # Controle de operações diárias por cliente
        self.operacoes_diarias = 0
        self.data_ultima_operacao = datetime.now().date()
        self.LIMITE_OPERACOES_DIA = 10

    def verificar_e_atualizar_data(self):
        """Verifica se é um novo dia e reseta o contador de operações"""
        hoje = datetime.now().date()
        if hoje != self.data_ultima_operacao:
            self.operacoes_diarias = 0
            self.data_ultima_operacao = hoje
            print(f"\n[Cliente {self.nome}] Novo dia iniciado! Contador de operações reiniciado.")
            print(f"Lembrando que você pode realizar até {self.LIMITE_OPERACOES_DIA} operações por dia.")
            return True
        return False

    def pode_realizar_operacao(self):
        """Verifica se o cliente pode realizar mais operações hoje"""
        self.verificar_e_atualizar_data()
        
        if self.operacoes_diarias >= self.LIMITE_OPERACOES_DIA:
            print(f"Operação não realizada! Cliente {self.nome} excedeu o limite de {self.LIMITE_OPERACOES_DIA} operações no dia de hoje.")
            return False
        return True

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao"):
        if not self.pode_realizar_operacao():
            return False
            
        sucesso = transacao.registrar(conta)
        if sucesso:
            self.operacoes_diarias += 1
            return True
        return False

    def exibir_extrato(self, conta: "Conta"):
        """Exibe o extrato de uma conta específica do cliente"""
        if not self.pode_realizar_operacao():
            return False
            
        data = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%H:%M")
        
        print("\n========================= EXTRATO =========================")
        print(conta.historico.imprimir_extrato())
        print(f"\nSaldo: R$ {conta.saldo:.2f} em {data}, às {hora}.")
        print(f"Operações realizadas hoje por {self.nome}: {self.operacoes_diarias + 1}")
        print("===========================================================")
        
        self.operacoes_diarias += 1
        return True

    def adicionar_conta(self, conta: "Conta"):
        self.contas.append(conta)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: "Transacao"):
        data = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%H:%M")
        transacao_com_data = f"{transacao.tipo}: R$ {transacao.valor:.2f} => Realizado em {data}, às {hora}.\n"
        self.transacoes.append(transacao_com_data)

    def imprimir_extrato(self):
        if not self.transacoes:
            return "Não foram realizadas movimentações."
        return "".join(self.transacoes)

class Conta:
    def __init__(self, cliente: Cliente, numero: int, agencia: str = "0001"):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        cliente.adicionar_conta(self)

    def saldo(self) -> float:
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int) -> "Conta":
        return cls(cliente, numero)

    def sacar(self, valor: float) -> bool:
        if valor > self.saldo:
            print("Operação não realizada! Conta não tem saldo suficiente.")
            return False
        
        self.saldo -= valor
        return True

    def depositar(self, valor: float) -> bool:
        self.saldo += valor
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, numero: int, limite: float = 500, limite_saques: int = 3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_diarios = 0
        self.data_ultimo_saque = datetime.now().date()

    def sacar(self, valor: float) -> bool:
        hoje = datetime.now().date()
        
        # Verifica se é um novo dia para resetar contador de saques
        if hoje != self.data_ultimo_saque:
            self.saques_diarios = 0
            self.data_ultimo_saque = hoje
        
        # Verifica limite de saques diários
        if self.saques_diarios >= self.limite_saques:
            print(f"Operação não realizada! Número máximo de {self.limite_saques} saques diários excedido.")
            return False
        
        # Verifica se o valor excede o limite por saque
        if valor > self.limite:
            print("Operação não realizada! Valor do saque excedeu o limite.")
            return False
        
        # Chama o método sacar da classe pai
        if super().sacar(valor):
            self.saques_diarios += 1
            return True
        
        return False

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @property
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
        self._tipo = "Depósito"
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def tipo(self):
        return self._tipo
    
    def registrar(self, conta: Conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
            print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso!")
            return True
        return False

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
        self._tipo = "Saque"

    @property
    def valor(self):
        return self._valor
    
    @property
    def tipo(self):
        return self._tipo
    
    def registrar(self, conta: Conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso!")
            return True
        return False

class SistemaBancario:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.agencia_padrao = "0001"
        self.proximo_numero_conta = 1

    def obter_valor(self, mensagem):
        """Função para obter valores numéricos"""
        while True:
            try:
                valor = float(input(mensagem))
                if valor <= 0:
                    print("Erro! O valor deve ser maior que zero.")
                    continue
                return valor
            except ValueError:
                print("Erro! Por favor, digite apenas números, substituindo a vírgula por ponto, se for o caso.\n")

    def buscar_cliente(self, cpf):
        """Busca cliente pelo CPF"""
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def depositar(self, cliente_cpf, conta_numero):
        """Realiza um depósito em uma conta"""
        # Busca a conta
        conta = self.buscar_conta(cliente_cpf, conta_numero)
        if not conta:
            print("Conta não encontrada!")
            return
        
        # Busca o cliente
        cliente = self.buscar_cliente(cliente_cpf)
        if not cliente:
            print("Cliente não encontrado!")
            return
        
        # Realiza o depósito
        valor = self.obter_valor("Informe o valor do depósito: ")
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)

    def sacar(self, cliente_cpf, conta_numero):
        """Realiza um saque em uma conta"""
        # Busca a conta
        conta = self.buscar_conta(cliente_cpf, conta_numero)
        if not conta:
            print("Conta não encontrada!")
            return
        
        # Busca o cliente
        cliente = self.buscar_cliente(cliente_cpf)
        if not cliente:
            print("Cliente não encontrado!")
            return
        
        # Realiza o saque
        valor = self.obter_valor("Informe o valor do saque: ")
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)

    def exibir_extrato(self, cliente_cpf, conta_numero):
        """Exibe o extrato de uma conta"""
        # Busca a conta
        conta = self.buscar_conta(cliente_cpf, conta_numero)
        if not conta:
            print("Conta não encontrada!")
            return
        
        # Busca o cliente
        cliente = self.buscar_cliente(cliente_cpf)
        if not cliente:
            print("Cliente não encontrado!")
            return
        
        # Exibe o extrato através do cliente
        cliente.exibir_extrato(conta)

    def criar_cliente(self):
        """Cria um novo cliente"""
        cpf = input("Informe o CPF (somente números): ")
        cliente = self.buscar_cliente(cpf)
        if cliente:
            print("\nJá existe cliente com esse CPF!")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
        
        # Cria pessoa física
        pessoa = PessoaFisica(cpf, nome, data_nascimento)
        
        # Cria o cliente
        novo_cliente = Cliente(pessoa, endereco)
        self.clientes.append(novo_cliente)
        
        print("Cliente cadastrado com sucesso!")

    def criar_conta(self):
        """Cria uma nova conta"""
        cpf = input("Informe o CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if cliente:
            # Cria a conta para o cliente
            conta = ContaCorrente(cliente, self.proximo_numero_conta)
            self.contas.append(conta)
            self.proximo_numero_conta += 1
            
            print(f"\nConta criada com sucesso! Número: {conta.numero}, Agência: {conta.agencia}")
            return
        
        print("\nCliente não encontrado! Não foi possível criar a conta. Verifique o CPF e tente novamente.")

    def buscar_conta(self, cpf, numero_conta=None):
        """Busca uma conta pelo CPF do cliente e opcionalmente pelo número da conta"""
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            return None
        
        if numero_conta is None and cliente.contas:
            # Se não especificar número da conta, retorna a primeira
            return cliente.contas[0]
        
        # Busca a conta específica
        for conta in cliente.contas:
            if conta.numero == numero_conta:
                return conta
                
        return None

    def selecionar_conta(self, cpf):
        """Permite ao usuário selecionar uma conta quando o cliente tem múltiplas contas"""
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            print("Cliente não encontrado!")
            return None
            
        if not cliente.contas:
            print("Cliente não possui contas!")
            return None
            
        if len(cliente.contas) == 1:
            return cliente.contas[0].numero
            
        print("\nContas disponíveis:")
        for i, conta in enumerate(cliente.contas):
            print(f"{i+1}. Conta {conta.numero} - Agência {conta.agencia}")
            
        while True:
            try:
                escolha = int(input("\nSelecione o número da opção da conta: "))
                if 1 <= escolha <= len(cliente.contas):
                    return cliente.contas[escolha-1].numero
                print("Opção inválida!")
            except ValueError:
                print("Por favor, digite um número válido.")

    def exibir_menu(self):
        menu = """
    ====== OPÇÕES ======

    [D]  Depositar
    [S]  Sacar
    [E]  Exibir Extrato
    [IC] Incluir Cliente
    [CC] Cadastar Conta
    [F]  Finalizar

    =>"""

        return input(menu).lower()

    def executar(self):
        """Método principal que executa o sistema bancário"""
        while True:
            opcao = self.exibir_menu()

            if opcao == "d":
                cpf = input("Informe o CPF do cliente: ")
                numero_conta = self.selecionar_conta(cpf)
                if numero_conta:
                    self.depositar(cpf, numero_conta)

            elif opcao == "s":
                cpf = input("Informe o CPF do cliente: ")
                numero_conta = self.selecionar_conta(cpf)
                if numero_conta:
                    self.sacar(cpf, numero_conta)

            elif opcao == "e":
                cpf = input("Informe o CPF do cliente: ")
                numero_conta = self.selecionar_conta(cpf)
                if numero_conta:
                    self.exibir_extrato(cpf, numero_conta)

            elif opcao == "ic":
                self.criar_cliente()

            elif opcao == "cc":
                self.criar_conta()

            elif opcao == "f":
                print("Obrigado por ser nosso(a) cliente!\n")
                break

            else:
                print("Operação inválida! Por favor, selecione corretamente a opção desejada.")

if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.executar()