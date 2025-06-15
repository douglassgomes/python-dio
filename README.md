# Python - Projetos do Bootcamp da DIO

## 🏦 Conta Bancária

### Escopo do Projeto (v4)

Este quarto projeto teve como objetivo a alteração do código em linguagem Python dos projetos anteriores (constantes nas outras branchs) de modo a implementar o seguinte:

- atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários, seguindo o modelo de classes UML abaixo.

![Diagrama UML](./docs/images/uml_desafio_python.png "Diagrama de Classes do Sistema Bancário (v4)")

### 💸📄 Operações e Condições

#### ⚠️ Limite geral de 10 operações diárias. (v2)
  
#### Depósito

- Não podem ocorrer depósitos de valores iguais ou menores que zero;
- Todos os depósitos devem ser registrados em extrato.

#### Saque

- São permitidos no máximo 3 saques;
- O limite máximo por saque é de R$ 500,00;
- Deve ser exibida mensagem informando que não é possível realizar o saque e o motivo;
- Todos os saques devem ser registrados em extrato.

#### Extrato

- Deve listar todos os depósitos e saques realizados;
- No fim da listagem deve ser exibido o saldo atual da conta;
- Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
- os valores devem ser exibidos utilizando o formato R$ XXX.XX. Exemplo: 1500.45 = R$ 1500.45

### 💡 Ajustes e Melhorias Implementados (v4)

1. Identificação das Classes Principais

    A partir do diagrama UML, identifiquei as classes principais:

    - PessoaFisica: Contém os dados básicos de uma pessoa (CPF, nome, data de nascimento)
    - Cliente: Representa um cliente do banco com seus dados e relação com suas contas
    - Conta: Classe base para contas bancárias
    - ContaCorrente: Especialização de Conta com limites de saque
    - Historico: Mantém o registro de transações
    - Transacao: Interface (classe abstrata) para diferentes tipos de transações
    - Deposito e Saque: Implementações concretas de Transacao

2. Transformação dos Dicionários em Objetos, pois no código original, os dados eram armazenados em dicionários simples.

3. Implementação do Padrão de Projeto Strategy

    Seguindo o diagrama UML implementei o uso do padrão Strategy para as transações, através da classe abstrata Transacao e suas subclasses Deposito e Saque, cada uma encapsulando seu comportamento específico.

4. Encapsulamento da Lógica

    Encapsulei a lógica das operações bancárias dentro das respectivas classes:

    - A lógica de sacar foi movida para o método sacar() da classe Conta e especializada na ContaCorrente
    - A lógica de depositar foi movida para o método depositar() da classe Conta
    - O controle do histórico foi encapsulado na classe Historico

5. Organização do Fluxo Principal

    Criei uma classe SistemaBancario que organiza o fluxo principal do programa, substituindo a função main() do código original. Isso permite:

    - Melhor organização do código
    - Manutenção do estado do sistema em atributos de classe
    - Possibilidade de instanciar múltiplos sistemas, se necessário no futuro.

6. Outras Melhorias Implementadas

    Além da transformação para Orientação a Objetos, implementei algumas outras melhorias:

    - Tipagem: Utilizei type hints para melhorar a legibilidade e robustez do código
    - Seleção de Conta: Adicionei funcionalidade para selecionar entre múltiplas contas de um cliente
    - Abstração: Utilizei métodos abstratos para garantir implementação consistente de transações

7. Detalhes das Classes Implementadas

    - **PessoaFisica**: Armazena os dados básicos de identificação de uma pessoa.
    - **Cliente**: Encapsula a relação entre uma pessoa física e suas contas bancárias, bem como os métodos para realizar transações.
    - **Conta**: Classe base que implementa a funcionalidade comum a todos os tipos de conta:

        - Manutenção de saldo
        - Operações básicas de saque e depósito
        - Relação com cliente e histórico

    - **ContaCorrente**: Especialização de Conta que adiciona:

        - Limite de valor por saque
        - Controle do número de saques diários
        - Verificações adicionais durante operações de saque

    - **Historico**: Mantém registro das transações realizadas em uma conta.

    - **Transacao (e subclasses)**: Utiliza o padrão Strategy para encapsular os diferentes tipos de transações bancárias, com o método registrar() implementando a lógica específica de cada tipo.

    - **SistemaBancario**: Coordena as operações do sistema bancário, mantendo o estado do sistema e gerenciando a interação com o usuário.

### 🛠️ Tecnologias e Ferramentas Utilizadas

![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=yellow)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GNU/Linux/Debian](https://img.shields.io/badge/GNU/Linux/Debian-35495E?style=for-the-badge&logo=debian&logoColor=E44C30)
![/bin/bash](https://img.shields.io/badge/bash-5495E?style=for-the-badge&logo=shell&logoColor=fff)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/douglassgomes)

## Referências

- [Digital Inovation One - DIO](https://web.dio.me/)
- [Repositório DIO - Trilha Python](https://github.com/digitalinnovationone/trilha-python-dio)
- [Documentação do Python](https://docs.python.org)

</br>[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)



