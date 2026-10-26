nomes = []
precos = []
def mostrar_menu(): 
    print("\n === PAPELARIA PONTO CERTO ===")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("0 - Sair")
def cadastrar_produto():
    nome = input ("Nome do Produto: ")
    preco = float (input("Informe o Preço do Produto: "))
    if preco <= 0:
        print("Preço Inválido!")
        #FORA LULA MALDITO; OUTUBRO VIOLETA, TODOS JUNTO CONTRA O CAPETA
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
while opcao != "0":
    mostrar_menu()
    opcao = input("Escolha: ")
    if opcao =="1":
        cadastrar_produto()
    elif opcao == "2":
        consultar_produtos()
    elif opcao == "0":
        print ("Encerrando. . .")
    else:
        print ("Opção Inválida!")