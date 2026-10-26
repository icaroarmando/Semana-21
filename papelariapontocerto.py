nomes = []
precos = []
vendas = []

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

def registrar_venda():
    nome = input("Produto vendido: ")

    if nome in nomes:
        quantidade = int(input("Quantidade vendida: "))
        if quantidade > 0:
            vendas.append([nome, quantidade])
            print("Venda registrada!")
        else:
            print("Quantidade inválida!")
    else:
        print("Produto não cadastrado!")
def calcular_desempenho():
    nome = input("Informe o produto que quer analisar: ")
    quantidades = []

    for venda in vendas:
        if venda[0] == nome:
            quantidades.append(venda[1])

    if len(quantidades) == 0:
        print("Sem histórico de vendas!")
    else:
        media = sum(quantidades) / len(quantidades)
        total = sum(quantidades)
        print (f"Foram vendidas {total} unidades de {nome}")

        if media >= 30:
            desempenho = "Alto"
        elif media >= 10 and media <30:
            desempenho = "Médio"
        else:
            desempenho = "Baixo"

        print(f"Média: {media:.2f}")
        print(f"Desempenho: {desempenho}")

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