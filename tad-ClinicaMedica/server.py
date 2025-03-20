
pacientesNaoUrgentes = []
pacientesUrgentes = []
pacienteAtendidos = []

def menu():
    print("\nColoque a sua opção de navegação: \n")
    print("1 - Entrada de paciente")
    print("2 - Listar pacientes")
    print("6 - Sair \n")

    opcao = input()

    if opcao == "1":
        entradaPaciente()
    elif opcao == "2":
        listarPacientes()
    elif opcao == "6":
        print("Obrigado por usar o sistema!")
    else:
        print("Obrigado por usar o sistema!")

def adicionar_pacientes(namePaciente,numCarteirinha,sintomas,urgencia):
    paciente = {
        "nome": namePaciente,
        "carteira": numCarteirinha,
        "sintomas": sintomas,
        "urgencia": int(urgencia)
    }

    if int(urgencia) >= 6:
        pacientesUrgentes.append(paciente)
    else: 
       pacientesNaoUrgentes.append(paciente)

    print("Paciente protocolado com sucesso")

def entradaPaciente():
    print("Nome do paciente:")
    namePaciente = input()
    print("Numero da carteirinha:")
    numCarteirinha = input()
    print("Descreva is sintomas:")
    sintomas = input()
    print("Descreva a urgencia entre: 1 - 10")
    urgencia = input() 

    adicionar_pacientes(namePaciente,numCarteirinha,sintomas,urgencia)
    
    menu()

def listarPacientes():
    print("Pacientes urgentes:\n")
    for dadosPacienteUrgentes in pacientesUrgentes:
        print(dadosPacienteUrgentes)
    print("\n")

    print("Pacientes não urgentes:\n")
    for dadosPaciente in pacientesNaoUrgentes:
        print(dadosPaciente) 
    print("\n")

menu()

def triagem():
    print("Chamando paciente...\n")


print("Bem vindo ao ao sistema clinico de triagem:")
menu()






