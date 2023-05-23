#id = [1, 3]
#produtos = ["Banana", "Notebook"]
#qtd = [20, 2]
#validade = [3, -1]
#lote = [12345, 54321]
#valor_compra = [1.0, 3500.0]
#data_entrada = ["18/03/2023", "01/01/2023"]
#data_saida = ["", ""]
#valor_atual = [1, 3000]
#departamento = ["Copa", "RH"]
#filial = ["São Paulo", "São Paulo"]

produtos = {1:["Banana", 20, 3, 12345, 1.0, "18/03/2023", "", 1, "Copa", "SP"], 
            2:["Notebook", 2, -1, 54321, 3500.0, "01/01/2023", "", 3000, "RH", "SP"]}

def adicionar():
    id = list(produtos.keys())
    preco = float(input("Entre com o preço produto: "))
    produtos[id[len(id)-1]+1] = [input("Entre com o nome do produto: ").title(), 
                                int(input("Entre com o quantidade do produto: ")),
                                int(input("Entre com o validade produto: ")), 
                                int(input("Entre com o lote produto: ")),
                                preco, input("Entre com a data de entrada do produto: "), "",
                                preco, input("Entre com o nome do departamento: "), 
                                input("Entre com o nome da filial: ")]
    #produtos.append(input("Entre com o nome do produto: ").title())
    #qtd.append(int(input("Entre com o quantidade do produto: ")))
    #validade.append(int(input("Entre com o validade produto: ")))
    #lote.append(int(input("Entre com o lote produto: ")))
    #valor_compra.append(preco)
    #data_entrada.append(input("Entre com a data de entrada do produto: "))
    #data_saida.append("")
    #valor_atual.append(preco)
    #departamento.append(input("Entre com o nome do departamento: "))
    #filial.append(input("Entre com o nome da filial: "))

def relatorio():
    for index, lista in produtos.items:
        print("\nID:..................", index)
        print("Nome:................", lista[0])
        print("Quantidade:..........", lista[1])
        if lista[2] < 0:
            tempo = "Produto sem validade definida"
        else:
            tempo = str(lista[2])
        print("Validade:............", tempo)
        print("Lote:................", lista[3])
        print("Valor de compra:.....", lista[4])
        print("Data de entrada:.....", lista[5])
        if lista[6] == "":
            tmp = "Produto não vendido!"
        else:
            tmp = lista[6]
        print("Data de Saida:.......", tmp)
        print("Valor Atualizado:....", lista[7])
        print("Valor total alocado:.", (int(lista[4])*int(lista[1])))
        print("Departamento:........", lista[8])
        print("Filial:..............", lista[9])
def busca():
    busca = input("Entre com o nome do produto: ").title()
    for index,lista in produtos.items():
        if busca == lista[0]:
            print("\nID:..................", index)
            print("Nome:................", lista[0])
            print("Quantidade:..........", lista[1])
            if lista[2] < 0:
                tempo = "Produto sem validade definida"
            else:
                tempo = str(lista[2])
            print("Validade:............", tempo)
            print("Lote:................", lista[3])
            print("Valor de compra:.....", lista[4])
            print("Data de entrada:.....", lista[5])
            if lista[6] == "":
                tmp = "Produto não vendido!"
            else:
                tmp = lista[6]
            print("Data de Saida:.......", tmp)
            print("Valor Atualizado:....", lista[7])
            print("Valor total alocado:.", (int(lista[4])*int(lista[1])))
            print("Departamento:........", lista[8])
            print("Filial:..............", lista[9])
        else:
            print("Produto fora de estoque!")

def alterar():
    altera = input("Entre com o nome do produto: ").title()
    for index,lista in produtos.items():
        if busca == lista[0]:
            print("\nID:..................", index)
            print("Nome:................", lista[0])
            print("Quantidade:..........", lista[1])
            if lista[2] < 0:
                tempo = "Produto sem validade definida"
            else:
                tempo = str(lista[2])
            print("Validade:............", tempo)
            print("Lote:................", lista[3])
            print("Valor de compra:.....", lista[4])
            print("Data de entrada:.....", lista[5])
            if lista[6] == "":
                tmp = "Produto não vendido!"
            else:
                tmp = lista[6]
            print("Data de Saida:.......", tmp)
            print("Valor Atualizado:....", lista[7])
            print("Valor total alocado:.", (int(lista[4])*int(lista[1])))
            print("Departamento:........", lista[8])
            print("Filial:..............", lista[9])
        else:
            print("Produto fora de estoque!")

def remover():
    produtos.remove(input("entre com o produto a remover: "))
    #del produtos[0]

def vender():
    ...
  


remover