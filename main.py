contatos = {}

def adicionar_contato(nome, telefone):
    if nome in contatos:
        print(f"O contato {nome} já existe.")
    else:
        contatos[nome] = telefone
        print(f"Contato {nome} adicionado com sucesso.")

def visualizar_contatos():
    if contatos:
        for nome, telefone in contatos.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("Nenhum contato encontrado.")

def remover_contato(nome):
    if nome in contatos:
        del contatos[nome]
        print(f"Contato {nome} removido com sucesso.")
    else:
        print(f"Contato {nome} não encontrado.")

def menu():
    while True:
        print("\n1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Remover Contato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(nome, telefone)
        elif opcao == '2':
            visualizar_contatos()
        elif opcao == '3':
            nome = input("Digite o nome do contato a ser removido: ")
            remover_contato(nome)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()

