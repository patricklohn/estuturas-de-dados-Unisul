
pacientesNaoUrgentes = []
pacientesUrgentes = []
pacienteAtendidos = []
intervalPaciente = 0
pacientesAtendidos = []

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
    if not pacientesUrgentes[0]:
        intervalPaciente = 1
    elif not pacientesNaoUrgentes[0]:
        intervalPaciente = 0
        print("Não existe pacientes na triagem:") 
        return menu()
    else:
        print("Chamando paciente...\n")
    if intervalPaciente == 0: 
        print("Paciente urgente:", pacientesUrgentes[0].get("nome"))
        print("Numero Carteirinha:", pacientesUrgentes[0].get("carteira"))
        print("Sintomas reportados:", pacientesUrgentes[0].get("sintomas"))

        pacienteAtendidos.append(pacientesUrgentes[0])
        pacientesUrgentes.pop(0)
        print("Paciente Atendido com sucesso!")
    elif intervalPaciente == 1:
        print("Paciente:", pacientesNaoUrgentes[0].get("nome"))
        print("Numero:", pacientesNaoUrgentes[0].get("carteira"))
        print("Sintomas:", pacientesNaoUrgentes[0].get("sintomas"))

        pacienteAtendidos.append(pacientesNaoUrgentes[0])
        pacientesNaoUrgentes.pop(0)
        print("Paciente Atendido com sucesso!\n")
    print("Triagem finalizada com sucesso!\n")
    menu()
    


print("Bem vindo ao ao sistema clinico de triagem:")
menu()






