nomes = []
precos = []
def mostrar_menu(): 
    print("\n === PAPELARIA PONTO CERTO ===")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Listar todos os produtos")
    print("0 - Sair")
def cadastrar_produto():
    nome = input ("Nome do Produto: ")
    preco = float (input("Informe o Preço do Produto: "))
    if preco <= 0:
        print("Preço Inválido!")

    else:
        nomes.append(nome)
        precos.append(preco)
        print ("Produto Cadastrado")
def consultar_produtos():
    busca = input("Nome do produto: ")
    if busca in nomes:
        i = nomes.index(busca)
        print(f"{nomes[i]} - R$ {precos[i]:.2f}")
    else:
        print("Produto não encontrado!")
opcao = ""
def listar_produtos():
    if len(nomes) == 0:
        print("Nenhum produto cadastrado!")
    else:
        for i in range(len(nomes)):
            print(f"{nomes[i]} - R$ {precos[i]:.2f}")

while opcao != "0":
    mostrar_menu()
    opcao = input("Escolha: ")
    if opcao =="1":
        cadastrar_produto()
    elif opcao == "2":
        consultar_produtos()
    elif opcao == "3":
        listar_produtos()
    elif opcao == "0":
        print("Encerrando. . .")
    else:
        print ("Opção Inválida!")