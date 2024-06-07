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
      
