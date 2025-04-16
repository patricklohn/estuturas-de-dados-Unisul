class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(no, valor):
    if no is None:
        return No(valor)

    if valor < no.valor:
        no.esquerda = inserir(no.esquerda, valor)
    elif valor > no.valor:
        no.direita = inserir(no.direita, valor)

    return no

def em_ordem(no):
    if no is not None:
        em_ordem(no.esquerda)
        print(no.valor, end=' ')
        em_ordem(no.direita)

# Criando a árvore e inserindo valores
raiz = None
valores = [20, 2, 4, 25, 30, 7, 40]

for v in valores:
    raiz = inserir(raiz, v)

print("Árvore em ordem (ordenada):")
em_ordem(raiz)