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

