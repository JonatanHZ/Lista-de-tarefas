# Estrurua dos dados
tarefas = [{"titulo": "Estudar Python", "concluida": False}]

# Funções das tarefas
def adicionar_tarefa():
    titulo = input("Digite a tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    print("\n Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        marca = "x" if tarefa["concluida"] else " "
        print(f"{numero}. [{marca}] {tarefa['titulo']}")

# função que mostra as tarefas que foram concluidas 
def concluir_tarefa():
    listar_tarefas()
    if not tarefas:
        return

    try:
        numero = int(input("Número da tarefa concluida: "))
        tarefas[numero - 1]["concluida"] = True
        print("Tarefa concluida!")
    except (ValueError, IndexError):
        print("Número invalido.")

# função que remove e mostra o numero da tarefa removida 
def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return

    try:
        numero = int(input("Número da tarefa para remover: "))
        removida = tarefas.pop(numero - 1)
        print(f"tarefa '{removida['titulo']}' removida.")
    except (ValueError, IndexError):
        print("Número inválido.")

# criação do menu 
def menu():
    while True:
        print("\n=== LISTA DE TAREFAS ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. concluir tarefa")
        print("4. Remover tarefa")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "0":
            print("Até mais!!")
            break
        else:
            print("opcão inválida!")
menu()