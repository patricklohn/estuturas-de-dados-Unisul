
paciente = []

class Paciente: 
    def __init__(self, nome, numCarteirinha, sintomas, urgencia):
        self.nome = nome
        self.numCarteirinha = numCarteirinha
        self.sintomas = sintomas
        self.urgencia = urgencia

def entradaPaciente():
    print("Nome do paciente:")
    namePaciente = input()
    print("Numero da carteirinha:")
    numCarteirinha = input()
    print("Descreva is sintomas:")
    sintomas = input()
    print("Descreva a urgencia entre: 1 - 10")
    urgencia = input()



def chamadaCliente():
    print("Teste")

