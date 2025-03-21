# Sistema Clínico de Triagem

Este é um sistema simples de triagem de pacientes escrito em **Python**. Ele permite cadastrar pacientes, listar pacientes registrados e realizar a triagem para atendimento.

## Funcionalidades

- **Cadastro de Pacientes**: Permite adicionar pacientes ao sistema informando nome, carteirinha, sintomas e nível de urgência.
- **Listagem de Pacientes**: Exibe todos os pacientes cadastrados, separados em urgentes, não urgentes e atendidos.
- **Triagem**: Atende os pacientes seguindo a prioridade de urgência.

## Como Usar

### Requisitos

- Python 3 instalado no sistema

### Executando o programa

1. Salve o arquivo como `server.py`.
2. Abra o terminal ou prompt de comando.
3. Navegue até a pasta onde o arquivo está salvo.
4. Execute o comando:
   ```bash
   python server.py
   ```

### Opções do Menu

Ao iniciar o programa, o usuário pode escolher uma das seguintes opções:

1. **Entrada de paciente**: Solicita informações do paciente e adiciona ao sistema.
2. **Listar pacientes**: Exibe a lista de pacientes em diferentes categorias (urgentes, não urgentes e atendidos).
3. **Triagem**: Atende os pacientes com base na prioridade de urgência.
4. **Sair**: Encerra o programa.

## Estrutura do Código

O programa utiliza listas para armazenar os pacientes:

- `pacientesUrgentes`: Armazena pacientes com urgência **≥ 6**.
- `pacientesNaoUrgentes`: Armazena pacientes com urgência **< 6**.
- `pacienteAtendidos`: Armazena pacientes já atendidos.

O atendimento é realizado prioritariamente para pacientes urgentes. Se não houver pacientes urgentes, pacientes não urgentes serão chamados.

## Possíveis Melhorias

- Adicionar persistência de dados (ex: salvar os pacientes em um arquivo JSON ou banco de dados).
- Melhorar a interface com uma versão em **Tkinter** ou **Flask**.
- Implementar autenticação para controle de acesso.

---

**Autor:** **Patrick Lohn**

