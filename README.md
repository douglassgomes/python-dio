# Python - Projetos do Bootcamp da DIO

## 🏦 Conta Bancária

### Escopo do Projeto

Este primeiro projeto teve como objetivo a criação de um código em linguagem Python para realizar operações simples em uma conta bancária.

### 💸📄 Operações e Condições (Iniciais)

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

### 💡 Ajustes e Melhorias Implementados

Além das condições inicialmente propostas, adicionei algumas melhorias, tais como:
- O código foi segmentado de modo que cada operação fosse realizada por uma **função**;
- Adicionado bloco **try / exception** para tratar a entrada de valores diferentes de números nas operações de depósito e saque, exibindo mensagem de orientação em caso de erro do usuário;
- Adicionada conversão para minúsculo da entrada da opção de menu, evitando assim que que a opção não corresponda caso o usuário a digite em maiúscula;
- Adicionada mensagem de despedida, caso a opção finalizar seja selecionada.

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

</br>[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)



