# Pilhas na Estrutura de Dados: Gestão de Compras

## O que é uma Pilha?
Uma pilha é uma estrutura de dados que segue o princípio **LIFO (Last In, First Out)**, ou seja, o último elemento a ser inserido é o primeiro a ser removido. É como uma pilha de pratos: você adiciona um prato no topo e remove o último prato que foi colocado.

## Como as Pilhas são Utilizadas no Código?
No código, a pilha é usada para armazenar as entradas de compra de cada produto. Cada entrada é um dicionário que contém informações como data da compra, custo, margem de lucro, preço de venda e quantidade comprada.

### Funcionalidades da Pilha no Código

1. **Adicionar Compra (`adicionar_compra`)**:
   - Cada nova compra é adicionada ao topo da pilha usando o método `append`.
   - Isso garante que a última compra seja sempre a primeira a ser acessada.

2. **Estoque Atual (`estoque_atual`)**:
   - O estoque é calculado somando as quantidades de todas as entradas na pilha.
   - Isso permite rastrear o total de produtos disponíveis, independentemente de quantas compras foram feitas.

3. **Preço Atual (`preco_atual`)**:
   - O preço de venda é obtido a partir da última entrada na pilha (última compra).
   - Isso garante que o preço reflete o custo mais recente e a margem aplicada.

4. **Última Compra (`ultima_compra`)**:
   - Retorna os dados da última compra (último item da pilha).
   - Se a pilha estiver vazia, retorna `None`.

### Vantagens do Uso de Pilhas
- **Simplicidade**: A pilha é uma estrutura simples e eficiente para gerenciar entradas sequenciais.
- **Acesso Rápido**: O último item inserido pode ser acessado instantaneamente.
- **Rastreabilidade**: Permite rastrear o histórico de compras de cada produto.

### Exemplo de Funcionamento
Suponha que um produto tenha as seguintes compras:
1. **Compra 1**: Data = "01/01/2023", Custo = 10.0, Margem = 50%, Quantidade = 100.
2. **Compra 2**: Data = "15/01/2023", Custo = 12.0, Margem = 50%, Quantidade = 50.

A pilha ficaria assim:
```python
pilha = [
    {'data': '01/01/2023', 'custo': 10.0, 'venda': 15.0, 'margem': 50, 'quantidade': 100},
    {'data': '15/01/2023', 'custo': 12.0, 'venda': 18.0, 'margem': 50, 'quantidade': 50}
]