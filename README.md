# Desafio de Código - Sistema Bancário em Python
Pequeno desafio de código referente ao Bootcamp de Engenharia de Dados da NTT Data pelo DIO.

# Objetivo do Desafio
Criar um sistema bancário com as operações: depósito, saque e extrato.

| Operações de depósito | Operação de saque | Operação de extrato | 
| ----------------------- | ------------------- | --------------------- |
| Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos precoupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato. | O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato. | Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx. Ex:. 1500.45 = R$ 1500.45 |

# Conceitos utilizados no código
Para a criação do código foram utilizados os conceitos de manipulação de dados e strings, operadores condicionais `(if/elif/else)`, operadores de repetição `(while)` e `funções`.

# Solução do Código
O primeiro passo foi declarar as variaveis globais referentes ao saldo, extrato e saque, levando em consideração os limites de operações e valores de saque. Em seguida, foi criada a função que imprime o menu com as opções do banco, além das demais funções de depositar, sacar, e visualizar extrato. Por fim, foi criado um loop infinito utilizado o operador `while`, onde ele exibe o menu e pergunta qual operação será realizada. Com o uso dos operadores condicionais `(if, elif, else)`, foi determinado a função que será chamada de acordo com o que foi digitado. Finalizando, ao escolher a opção de sair, o sistema exibe uma mensagem de agradecimento e finaliza o loop, encerrando o programa.
