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

# Impressão visual da árvore
def imprimir_arvore(no, nivel=0, prefixo="Raiz: "):
    if no is not None:
        print(" " * (nivel * 4) + prefixo + str(no.valor))
        if no.esquerda or no.direita:
            imprimir_arvore(no.esquerda, nivel + 1, "L--- ")
            imprimir_arvore(no.direita, nivel + 1, "R--- ")

# Criando a árvore
raiz = None
valores = []

while True:
    entrada = input("Digite um número (ou 'sair' para parar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        valores.append(numero)
    except ValueError:
        print("Digite um número válido!")

print("Valores inseridos:", valores)

for v in valores:
    raiz = inserir(raiz, v)

# Mostrar estrutura da árvore
print("Estrutura da árvore:")
imprimir_arvore(raiz)
