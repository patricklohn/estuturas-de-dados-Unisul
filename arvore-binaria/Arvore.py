class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if no is None:
            return Node(valor)
        if valor < no.valor:
            no.esquerda = self._inserir_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir_recursivo(no.direita, valor)
        return no

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no, valor):
        if no is None:
            return None

        if valor < no.valor:
            no.esquerda = self._remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda

            sucessor = self._menor_valor(no.direita)
            no.valor = sucessor.valor
            no.direita = self._remover_recursivo(no.direita, sucessor.valor)

        return no

    def _menor_valor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def listar(self):
        elementos = []
        self._listar_recursivo(self.raiz, elementos)
        return elementos

    def _listar_recursivo(self, no, elementos):
        if no is not None:
            self._listar_recursivo(no.esquerda, elementos)
            elementos.append(no.valor)
            self._listar_recursivo(no.direita, elementos)

if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()

    while True:
        acao = input("Escolha uma ação: inserir (i), remover (r), listar (l), sair (s): ").lower()
        if acao == 'i':
            valor = int(input("Digite o valor para inserir: "))
            arvore.inserir(valor)
        elif acao == 'r':
            valor = int(input("Digite o valor para remover: "))
            arvore.remover(valor)
        elif acao == 'l':
            print("Elementos na árvore:", arvore.listar())
        elif acao == 's':
            break
        else:
            print("Ação inválida! Tente novamente.")