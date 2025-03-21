from colorama import Fore, Back, Style, init
init(autoreset=True)

pacientesNaoUrgentes = [{'nome': 'Erick', 'carteira': '147', 'sintomas': 'Dor de cabeça', 'urgencia': 5},{'nome': 'Rafael', 'carteira': '12347', 'sintomas': 'Muita febre', 'urgencia': 4}]
pacientesUrgentes = [{'nome': 'Patrick Lohn', 'carteira': '1234', 'sintomas': 'Muita tosse', 'urgencia': 8},{'nome': 'Andrey', 'carteira': '12345', 'sintomas': 'Gripe', 'urgencia': 8}]
pacienteAtendidos = []
global intervalPaciente
intervalPaciente = 0

def menu():
    print("\nColoque a sua opção de navegação: \n")
    print(Back.BLACK+ Style.BRIGHT +  "   1 - Entrada de paciente     ")
    print(Back.BLACK + Style.BRIGHT + "   2 - Listar pacientes        ")
    print(Back.BLACK + Style.BRIGHT + "   3 - Triagem                 ")
    print(Back.BLACK + Style.BRIGHT + "   6 - Sair                    " + Style.RESET_ALL + "\n")

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
    print("\n")
    namePaciente = input(Back.BLACK+Style.BRIGHT+  "   Nome do paciente:                 " + Style.RESET_ALL)
    numCarteirinha = input(Back.BLACK+Style.BRIGHT+"   Numero da carteirinha:            " + Style.RESET_ALL)
    sintomas = input(Back.BLACK+Style.BRIGHT+      "   Descreva os sintomas:             " + Style.RESET_ALL)
    urgencia = input(Back.BLACK+Style.BRIGHT+      "   Descreva a urgencia entre: 1 - 10 " + Style.RESET_ALL) 

    adicionar_pacientes(namePaciente,numCarteirinha,sintomas,urgencia)
    
    menu()

def listarPacientes():
    print("\n" + Back.RED + Style.BRIGHT + "   Pacientes urgentes:   " + Style.RESET_ALL + "\n")
    for dadosPacienteUrgentes in pacientesUrgentes:
        print(dadosPacienteUrgentes)

    print(Style.RESET_ALL + "\n" + Back.WHITE + Fore.BLACK + Style.BRIGHT +"   Pacientes não urgentes:   "+ Style.RESET_ALL + "\n")
    for dadosPaciente in pacientesNaoUrgentes:
        print(dadosPaciente) 

    print(Style.RESET_ALL + "\n" + Back.GREEN + Style.BRIGHT + "   Pacientes Atendidos:   "+ Style.RESET_ALL + "\n")
    for dadosPaciente in pacienteAtendidos:
        print(dadosPaciente) 
    print(Style.RESET_ALL + "\n")

    menu()

def triagem():
    if not pacientesUrgentes and not pacientesNaoUrgentes:
        print("\n" + Back.RED + Style.BRIGHT +"   Não existe pacientes na triagem:   " + Style.RESET_ALL + "\n") 
        return menu()
    
    if not pacientesUrgentes:
        intervalPaciente = 2
        print(Style.RESET_ALL + "\n" + Back.GREEN + Style.BRIGHT + "   Chamando paciente...   " + Style.RESET_ALL + "\n")

    elif not pacientesNaoUrgentes:
        intervalPaciente = 0
        print(Style.RESET_ALL + "\n" + Back.GREEN + Style.BRIGHT + "   Chamando paciente...   " + Style.RESET_ALL + "\n")

    else:
        intervalPaciente = 0

    if intervalPaciente == 0 or intervalPaciente == 1: 
        print(Style.RESET_ALL + "\n" + Back.GREEN + Style.BRIGHT + "   Chamando paciente...   " + Style.RESET_ALL + "\n")
        print("Paciente urgente:", pacientesUrgentes[0].get("nome"))
        print("Numero Carteirinha:", pacientesUrgentes[0].get("carteira"))
        print("Sintomas reportados:", pacientesUrgentes[0].get("sintomas"))

        pacienteAtendidos.append(pacientesUrgentes[0])
        pacientesUrgentes.pop(0)
        intervalPaciente += 1
        print(Style.RESET_ALL + "\n" + Back.GREEN + Style.BRIGHT + "   Paciente Atendido com sucesso!   " + Style.RESET_ALL + "\n")
        return menu()

    elif intervalPaciente == 2:
        print(Style.RESET_ALL + "\n" + Back.GREEN + Style.BRIGHT + "   Chamando paciente...   " + Style.RESET_ALL + "\n")
        print("Paciente:", pacientesNaoUrgentes[0].get("nome"))
        print("Numero:", pacientesNaoUrgentes[0].get("carteira"))
        print("Sintomas:", pacientesNaoUrgentes[0].get("sintomas"))

        pacienteAtendidos.append(pacientesNaoUrgentes[0])
        pacientesNaoUrgentes.pop(0)
        intervalPaciente = 0
        print(Style.RESET_ALL + "\n" + Back.GREEN + Style.BRIGHT + "   Paciente Atendido com sucesso!   " + Style.RESET_ALL + "\n")
        return menu()
        
    else:
        print("Erro no software\n")
        return menu()
    

print("Bem vindo ao ao sistema clinico de triagem:")
menu()






