# Sistema de Avaliação de Devoluções

Este é um sistema simples para avaliação de pedidos de devolução. O script recebe as informações sobre os pedidos e compras, além do motivo da devolução. Em seguida, o departamento responsável insere uma resposta (aprovação ou recusa) com base na análise do pedido.

## Funcionalidade

O programa exibe as informações de dois pedidos de devolução e solicita ao usuário se o pedido deve ser aprovado ou recusado. Caso o pedido seja recusado, o usuário deve fornecer um motivo para a recusa.

- **Número do Pedido**
- **Número da Compra**
- **Descrição da Solicitação**

Para cada pedido, o departamento responsável insere o resultado da análise e, se recusado, um motivo para a recusa.

## Como Usar

1. Execute o script Python.
2. O script exibirá as informações de dois pedidos de devolução.
3. O departamento responsável deverá inserir **True** para aprovação ou **False** para recusa de cada pedido.
4. Se o pedido for recusado, será solicitado um motivo para a recusa.

## Exemplo de Execução

O Numero pedido: 1456 E o Numero da compra: 50 Com motivo: Devolvi pois estava quebrado! Escreva o resultado do departamento: True or False

O script solicitará a resposta do departamento para o primeiro pedido. Após isso, o mesmo processo será repetido para o segundo pedido.

## Estrutura do Código

- **Variáveis de Entrada:**
  - `numeroPedidoUm`, `numeroPedidoDois`: Número de identificação do pedido.
  - `numeroCompraUm`, `numeroCompraDois`: Número de identificação da compra.
  - `descricaoSolicitacaoUM`, `descricaoSolicitacaoDois`: Motivos das devoluções.

- **Lógica:**
  - O script solicita ao departamento se a devolução é **Aprovada** ou **Recusada**.
  - Se recusado, é solicitado um **motivo** para a recusa.

## Requisitos

- Python 3.x