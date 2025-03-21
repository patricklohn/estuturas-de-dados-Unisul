
pacientesNaoUrgentes = [{'nome': 'Erick', 'carteira': '147', 'sintomas': 'Dor de cabeça', 'urgencia': 5},{'nome': 'Rafael', 'carteira': '12347', 'sintomas': 'Muita febre', 'urgencia': 4}]
pacientesUrgentes = [{'nome': 'Patrick Lohn', 'carteira': '1234', 'sintomas': 'Muita tosse', 'urgencia': 8},{'nome': 'Andrey', 'carteira': '12345', 'sintomas': 'Gripe', 'urgencia': 8}]
pacienteAtendidos = []
global intervalPaciente
intervalPaciente = 0

def menu():
    print("\nColoque a sua opção de navegação: \n")
    print("1 - Entrada de paciente")
    print("2 - Listar pacientes")
    print("3 - Triagem")
    print("6 - Sair \n")

    opcao = input()

    if opcao == "1":
        entradaPaciente()
    elif opcao == "2":
        listarPacientes()
    elif opcao == "3":
        triagem()
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
    print("Descreva os sintomas:")
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

    print("Pacientes Atendidos:\n")
    for dadosPaciente in pacienteAtendidos:
        print(dadosPaciente) 
    print("\n")

    menu()

def triagem():
    if not pacientesUrgentes and not pacientesNaoUrgentes:
        print("Não existe pacientes na triagem:") 
        return menu()
    
    if not pacientesUrgentes:
        intervalPaciente = 2
        print("\nChamando paciente...\n")

    elif not pacientesNaoUrgentes:
        intervalPaciente = 0
        print("\nChamando paciente...\n")

    else:
        intervalPaciente = 0

    if intervalPaciente == 0 or intervalPaciente == 1: 
        print("Paciente urgente:", pacientesUrgentes[0].get("nome"))
        print("Numero Carteirinha:", pacientesUrgentes[0].get("carteira"))
        print("Sintomas reportados:", pacientesUrgentes[0].get("sintomas"))

        pacienteAtendidos.append(pacientesUrgentes[0])
        pacientesUrgentes.pop(0)
        intervalPaciente += 1
        print("Paciente Atendido com sucesso!")
        return menu()

    elif intervalPaciente == 2:
        print("Paciente:", pacientesNaoUrgentes[0].get("nome"))
        print("Numero:", pacientesNaoUrgentes[0].get("carteira"))
        print("Sintomas:", pacientesNaoUrgentes[0].get("sintomas"))

        pacienteAtendidos.append(pacientesNaoUrgentes[0])
        pacientesNaoUrgentes.pop(0)
        internalPaciente = 0
        print("Paciente Atendido com sucesso!\n")
        return menu()
        
    else:
        print("Erro no software\n")
        return menu()
    

print("Bem vindo ao ao sistema clinico de triagem:")
menu()






