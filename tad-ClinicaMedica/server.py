
paciente = {}
pacientesUrgentes = {}

def menu():
    print("Coloque a sua opção de navegação:")
    print("1 - Entrada de paciente")
    print("2 - Listar pacientes")
    print("6 - Sair ")

    opcao = input()

    if opcao == "1":
        entradaPaciente()
    elif opcao == "2":
        listarPacientes()
    elif opcao == "6":
        print("Obrigado por usar o sistema!")
    else:
        print("Obrigado por usar o sistema!")

def entradaPaciente():
    print("Nome do paciente:")
    namePaciente = input()
    print("Numero da carteirinha:")
    numCarteirinha = input()
    print("Descreva is sintomas:")
    sintomas = input()
    print("Descreva a urgencia entre: 1 - 10")
    urgencia = input() 

    if int(urgencia) >= 6:
        pacientesUrgentes[namePaciente] ={
            "carteira": numCarteirinha,
            "sintomas": sintomas,
            "urgencia": urgencia
        }
    else: 
        paciente[namePaciente] = {
            "carteira": numCarteirinha,
            "sintomas": sintomas,
            "urgencia": urgencia
        }
    print("Paciente protocolado com sucesso")
    menu()

def listarPacientes():
    print("Pacientes urgentes:")
    for key, value in pacientesUrgentes.items():
        print(key,value)
    print("Pacientes não urgentes:")
    for key, value in paciente.items():
        print(key,value)
    menu()

print("Bem vindo ao ao sistema clinico de triagem:")
menu()






