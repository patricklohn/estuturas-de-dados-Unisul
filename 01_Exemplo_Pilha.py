class Pilha:
    def __init__(self):
        """Inicializa uma pilha vazia"""
        self.itens = []

    def empilhar(self, item):
        """Adiciona um item ao topo da pilha"""
        self.itens.append(item)
        print(f"Empilhado: {item}")

    def desempilhar(self):
        """Remove e retorna o item do topo da pilha"""
        if not self.esta_vazia():
            item = self.itens.pop()
            print(f"Desempilhado: {item}")
            return item
        else:
            print("A pilha está vazia!")
            return None

    def esta_vazia(self):
        """Verifica se a pilha está vazia"""
        return len(self.itens) == 0

    def topo(self):
        """Retorna o elemento no topo da pilha sem remover"""
        return self.itens[-1] if not self.esta_vazia() else None

    def tamanho(self):
        """Retorna o tamanho da pilha"""
        return len(self.itens)

# Exemplo de uso
pilha = Pilha()

# Empilhando elementos
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)

# Mostrando o topo
print(f"Topo da pilha: {pilha.topo()}")

# Desempilhando elementos
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()

# Tentando desempilhar de uma pilha vazia
pilha.desempilhar()
