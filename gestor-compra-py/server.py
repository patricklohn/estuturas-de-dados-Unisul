import tkinter as tk
from tkinter import ttk, messagebox

class Produto:
    def __init__(self, descricao, data_compra, custo, margem, quantidade):
        self.descricao = descricao
        self.pilha = []
        self.adicionar_compra(data_compra, custo, margem, quantidade)

    def adicionar_compra(self, data_compra, custo, margem, quantidade):
        venda = custo * (1 + margem / 100)
        self.pilha.append({
            'data': data_compra,
            'custo': custo,
            'venda': venda,
            'margem': margem,
            'quantidade': quantidade
        })

    def estoque_atual(self):
        return sum(item['quantidade'] for item in self.pilha)

    def preco_atual(self):
        return self.pilha[-1]['venda'] if self.pilha else 0.0

    def ultima_compra(self):
        """Retorna os dados da última compra (último item da pilha)."""
        return self.pilha[-1] if self.pilha else None


class GestaoCompras:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Compras")
        self.root.state('zoomed')
        self.produtos = {}
        self.vendas = []
        self.tela_principal()

    def tela_principal(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)
        
        btn_novo = tk.Button(frame, text="Entrada de Produto", command=self.tela_entrada_produto)
        btn_novo.pack(side=tk.LEFT, padx=5)
        
        btn_lista = tk.Button(frame, text="Listagem de Produtos", command=self.tela_listagem_produtos)
        btn_lista.pack(side=tk.LEFT, padx=5)
        
        btn_vendas = tk.Button(frame, text="Efetuar Venda", command=self.tela_venda_produtos)
        btn_vendas.pack(side=tk.LEFT, padx=5)

        btn_lista_vendas = tk.Button(frame, text="Listagem de Vendas", command=self.tela_listagem_vendas)
        btn_lista_vendas.pack(side=tk.LEFT, padx=5)

    def tela_entrada_produto(self):
        janela = tk.Toplevel(self.root)
        janela.title("Entrada de Produto")
        janela.lift()  # Garante que a janela fique no topo
        janela.focus_force()  # Foca na janela

        tk.Label(janela, text="Pesquisar Produto").grid(row=0, column=0)
        entry_pesquisa = tk.Entry(janela)
        entry_pesquisa.grid(row=0, column=1)
        
        # Campos de entrada para novos produtos ou atualização
        tk.Label(janela, text="Descrição").grid(row=1, column=0)
        tk.Label(janela, text="Data Compra").grid(row=2, column=0)
        tk.Label(janela, text="Custo").grid(row=3, column=0)
        tk.Label(janela, text="Margem (%)").grid(row=4, column=0)
        tk.Label(janela, text="Quantidade").grid(row=5, column=0)

        entry_descricao = tk.Entry(janela)
        entry_data = tk.Entry(janela)
        entry_custo = tk.Entry(janela)
        entry_margem = tk.Entry(janela)
        entry_quantidade = tk.Entry(janela)

        entry_descricao.grid(row=1, column=1)
        entry_data.grid(row=2, column=1)
        entry_custo.grid(row=3, column=1)
        entry_margem.grid(row=4, column=1)
        entry_quantidade.grid(row=5, column=1)

        def buscar_produto():
            descricao = entry_pesquisa.get().strip()
            if descricao in self.produtos:
                produto = self.produtos[descricao]
                ultimo_item = produto.ultima_compra()

                entry_descricao.delete(0, tk.END)
                entry_descricao.insert(0, produto.descricao)
                entry_data.delete(0, tk.END)
                entry_custo.delete(0, tk.END)
                entry_custo.insert(0, ultimo_item['custo'] if ultimo_item else '')
                entry_margem.delete(0, tk.END)
                entry_margem.insert(0, ultimo_item['margem'] if ultimo_item else '')
                entry_quantidade.delete(0, tk.END)
                
                messagebox.showinfo("Produto Encontrado", f"Produto '{descricao}' encontrado! Complete os dados para nova entrada.")
            else:
                # Permite cadastrar um novo produto se não encontrado
                entry_descricao.delete(0, tk.END)
                entry_data.delete(0, tk.END)
                entry_custo.delete(0, tk.END)
                entry_margem.delete(0, tk.END)
                entry_quantidade.delete(0, tk.END)
                messagebox.showinfo("Novo Produto", f"Produto '{descricao}' não encontrado. Cadastre um novo produto.")
        
        btn_buscar = tk.Button(janela, text="Buscar", command=buscar_produto)
        btn_buscar.grid(row=0, column=2, padx=5)

        def salvar():
            descricao = entry_descricao.get().strip()
            data = entry_data.get().strip()
            try:
                custo = float(entry_custo.get())
                margem = float(entry_margem.get())
                quantidade = int(entry_quantidade.get())
            except ValueError:
                messagebox.showerror("Erro", "Insira valores numéricos válidos para custo, margem e quantidade.")
                return

            if descricao in self.produtos:
                # Atualiza a quantidade se o produto já existir
                self.produtos[descricao].adicionar_compra(data, custo, margem, quantidade)
                messagebox.showinfo("Sucesso", f"Entrada adicionada ao produto '{descricao}'! Quantidade atualizada.")
            else:
                # Cadastra um novo produto se não encontrado
                novo_produto = Produto(descricao, data, custo, margem, quantidade)
                self.produtos[descricao] = novo_produto
                messagebox.showinfo("Sucesso", f"Novo produto '{descricao}' cadastrado com sucesso!")

            janela.destroy()

        btn_salvar = tk.Button(janela, text="Salvar", command=salvar)
        btn_salvar.grid(row=6, column=0, columnspan=2, pady=10)

    def tela_venda_produtos(self):
        janela = tk.Toplevel(self.root)
        janela.title("Efetuar Venda")
        janela.lift()  # Garante que a janela fique no topo
        janela.focus_force()  # Foca na janela

        tk.Label(janela, text="Nome do Cliente").grid(row=0, column=0)
        entry_cliente = tk.Entry(janela)
        entry_cliente.grid(row=0, column=1)

        tk.Label(janela, text="Pesquisar Produto").grid(row=1, column=0)
        entry_pesquisa = tk.Entry(janela)
        entry_pesquisa.grid(row=1, column=1)

        tk.Label(janela, text="Quantidade").grid(row=2, column=0)
        entry_quantidade = tk.Entry(janela)
        entry_quantidade.grid(row=2, column=1)

        # Lista de produtos adicionados à venda
        lista_produtos_venda = []

        # Treeview para exibir os produtos adicionados à venda
        tree = ttk.Treeview(janela, columns=("produto", "preco", "quantidade"), show='headings')
        tree.heading("produto", text="Produto")
        tree.heading("preco", text="Preço de Venda")
        tree.heading("quantidade", text="Quantidade")
        tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        def buscar_produto():
            descricao = entry_pesquisa.get().strip()
            if descricao in self.produtos:
                produto = self.produtos[descricao]
                preco_venda = produto.preco_atual()
                entry_pesquisa.delete(0, tk.END)
                entry_pesquisa.insert(0, descricao)
                entry_quantidade.delete(0, tk.END)
                messagebox.showinfo("Produto Encontrado", f"Produto '{descricao}' encontrado! Preço de venda: R${preco_venda:.2f}")
            else:
                messagebox.showerror("Erro", "Produto não encontrado.")

        btn_buscar = tk.Button(janela, text="Buscar Produto", command=buscar_produto)
        btn_buscar.grid(row=1, column=2, padx=5)

        def adicionar_produto_venda():
            descricao = entry_pesquisa.get().strip()
            quantidade = entry_quantidade.get().strip()

            if not descricao or not quantidade:
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            try:
                quantidade = int(quantidade)
            except ValueError:
                messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")
                return

            if descricao in self.produtos:
                produto = self.produtos[descricao]
                estoque = produto.estoque_atual()
                if quantidade > estoque:
                    messagebox.showerror("Erro", "Quantidade excede o estoque.")
                    return

                preco_venda = produto.preco_atual()
                lista_produtos_venda.append((descricao, preco_venda, quantidade))
                tree.insert("", tk.END, values=(descricao, preco_venda, quantidade))

                entry_pesquisa.delete(0, tk.END)
                entry_quantidade.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Produto não encontrado.")

        btn_adicionar = tk.Button(janela, text="Adicionar à Venda", command=adicionar_produto_venda)
        btn_adicionar.grid(row=2, column=2, padx=5)

        def registrar_venda():
            cliente = entry_cliente.get().strip()
            if not cliente:
                messagebox.showerror("Erro", "Informe o nome do cliente.")
                return

            if not lista_produtos_venda:
                messagebox.showerror("Erro", "Adicione pelo menos um produto à venda.")
                return

            total_venda = 0
            for produto, preco, quantidade in lista_produtos_venda:
                total_venda += preco * quantidade

                # Atualizar o estoque do produto
                self.produtos[produto].pilha[-1]['quantidade'] -= quantidade

                # Registrar a venda
                self.vendas.append({
                    'produto': produto,
                    'cliente': cliente,
                    'quantidade': quantidade,
                    'preco': preco,
                    'total': preco * quantidade
                })

            messagebox.showinfo("Venda Registrada", f"Venda registrada com sucesso! Total: R${total_venda:.2f}")
            janela.destroy()

        btn_registrar_venda = tk.Button(janela, text="Registrar Venda", command=registrar_venda)
        btn_registrar_venda.grid(row=4, column=0, columnspan=3, pady=10)

    def tela_listagem_produtos(self):
        janela = tk.Toplevel(self.root)
        janela.title("Listagem de Produtos")
        janela.lift()  # Garante que a janela fique no topo
        janela.focus_force()  # Foca na janela
        
        tree = ttk.Treeview(janela, columns=("descricao", "custo", "venda", "quantidade", "data", "margem"), show='headings')
        tree.heading("descricao", text="Descrição")
        tree.heading("custo", text="Custo")
        tree.heading("venda", text="Venda")
        tree.heading("quantidade", text="Quantidade")
        tree.heading("data", text="Data da Compra")
        tree.heading("margem", text="Margem")
        tree.pack(fill=tk.BOTH, expand=True)

        for produto in self.produtos.values():
            ultimo_item = produto.ultima_compra()
            if ultimo_item:
                tree.insert("", tk.END, values=(
                    produto.descricao, 
                    ultimo_item['custo'], 
                    ultimo_item['venda'], 
                    produto.estoque_atual(), 
                    ultimo_item['data'], 
                    ultimo_item['margem']
                ))

    def tela_listagem_vendas(self):
        janela = tk.Toplevel(self.root)
        janela.title("Listagem de Vendas")
        janela.lift()  # Garante que a janela fique no topo
        janela.focus_force()  # Foca na janela
        
        tree = ttk.Treeview(janela, columns=("cliente", "produto", "quantidade", "preco", "total"), show='headings')
        tree.heading("cliente", text="Cliente")
        tree.heading("produto", text="Produto")
        tree.heading("quantidade", text="Quantidade")
        tree.heading("preco", text="Preço Unitário")
        tree.heading("total", text="Total")
        tree.pack(fill=tk.BOTH, expand=True)

        for venda in self.vendas:
            tree.insert("", tk.END, values=(
                venda['cliente'], 
                venda['produto'], 
                venda['quantidade'], 
                venda['preco'], 
                venda['total']
            ))

root = tk.Tk()
app = GestaoCompras(root)
root.mainloop()