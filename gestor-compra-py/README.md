# Sistema de Gestão de Compras e Vendas

Este é um sistema de gestão de compras e vendas desenvolvido em Python utilizando a biblioteca `tkinter` para a interface gráfica. O sistema permite:
- Cadastrar produtos com informações como descrição, custo, margem de lucro e quantidade.
- Registrar entradas de compras para atualizar o estoque.
- Efetuar vendas, atualizando o estoque e registrando os detalhes da venda.
- Listar produtos e vendas realizadas.

## Estrutura do Projeto

### Classes Principais

#### 1. `Produto`
Representa um produto no sistema. Cada produto possui:
- **Descrição**: Nome ou identificação do produto.
- **Pilha de Compras**: Uma lista que armazena o histórico de compras do produto.
- **Métodos**:
  - `adicionar_compra`: Adiciona uma nova compra à pilha.
  - `estoque_atual`: Retorna a quantidade total em estoque.
  - `preco_atual`: Retorna o preço de venda atual.
  - `ultima_compra`: Retorna os dados da última compra.

#### 2. `GestaoCompras`
Gerencia a interface gráfica e a lógica do sistema. Possui:
- **Atributos**:
  - `produtos`: Dicionário que armazena os produtos cadastrados.
  - `vendas`: Lista que armazena as vendas realizadas.
- **Métodos**:
  - `tela_principal`: Exibe a tela principal com opções para o usuário.
  - `tela_entrada_produto`: Tela para cadastrar ou atualizar produtos.
  - `tela_venda_produtos`: Tela para registrar vendas.
  - `tela_listagem_produtos`: Tela para listar todos os produtos cadastrados.
  - `tela_listagem_vendas`: Tela para listar todas as vendas realizadas.

### Funcionalidades

#### 1. Cadastro de Produtos
- Permite cadastrar novos produtos ou atualizar o estoque de produtos existentes.
- Cada produto pode ter múltiplas entradas de compra, armazenadas em uma pilha.

#### 2. Registro de Vendas
- Permite registrar vendas de produtos, atualizando automaticamente o estoque.
- Cada venda pode incluir múltiplos produtos.

#### 3. Listagem de Produtos e Vendas
- Exibe uma lista de todos os produtos cadastrados, com informações como custo, preço de venda, estoque e margem de lucro.
- Exibe uma lista de todas as vendas realizadas, com detalhes como cliente, produtos vendidos e valor total.

### Como Executar o Projeto

1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Biblioteca `tkinter` (já incluída na instalação padrão do Python).

2. **Passos**:
   - Clone o repositório ou baixe o arquivo `gestao_compras.py`.
   - Execute o arquivo Python:
     ```bash
     python gestao_compras.py
     ```
   - A interface gráfica será aberta, permitindo interagir com o sistema.

### Exemplo de Uso

1. **Cadastrar um Produto**:
   - Na tela principal, clique em "Entrada de Produto".
   - Preencha os campos com as informações do produto e clique em "Salvar".

2. **Registrar uma Venda**:
   - Na tela principal, clique em "Efetuar Venda".
   - Pesquise o produto, insira a quantidade e clique em "Adicionar à Venda".
   - Repita o processo para adicionar mais produtos à venda.
   - Clique em "Registrar Venda" para finalizar.

3. **Listar Produtos e Vendas**:
   - Na tela principal, clique em "Listagem de Produtos" ou "Listagem de Vendas" para visualizar as informações.

### Pilhas na Estrutura de Dados

O sistema utiliza pilhas para gerenciar o histórico de compras de cada produto. Cada nova compra é adicionada ao topo da pilha, e o estoque é calculado somando as quantidades de todas as compras. O preço de venda é sempre obtido a partir da última compra registrada.

#### Vantagens:
- **Simplicidade**: Fácil de implementar e entender.
- **Eficiência**: Acesso rápido ao último item inserido.
- **Rastreabilidade**: Histórico completo de compras.

### Contribuição

Se você deseja contribuir para este projeto, siga os passos abaixo:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Contato

Se tiver dúvidas ou sugestões, entre em contato:
- **Email**: seuemail@exemplo.com
- **GitHub**: [seu-usuario](https://github.com/seu-usuario)