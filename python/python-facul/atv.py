camiseta_time = {1:["Camiseta do Flamengo", "Flamengo", "Camiseta", "Camiseta do Flamengo do ano de 2020", 250.0, 50, "Dry Fit"], 
                 2:["Moletom do PSG", "PSG", "Moletom", "Camiseta do PSG do ano de 2023", 200.0, 80, "Algodão"]}

def relatorio(): 
    for index, lista in camiseta_time.items():
        print("\nID:..................", index) 
        print("nome:..................", lista[0]) 
        print("Time:    ''................", lista[1]) 
        print("Tipo do produto:..................", lista[2]) 
        print("Descrição:..................", lista[3]) 
        print("Valor:..................", lista[4]) 
        print("Quantidade:..................", lista[5]) 
        print("Material:..................", lista[6])  
#relatorio()

def busca():
    escolha = int(input("Se deseja buscar atráves do ID(digite 1), se quer buscar pelo nome(digite 2): "))
    if escolha == 1:
        buscarId = int(input("Entre com o ID do produto: ").title()) 
        if buscarId == camiseta_time[buscarId]:
            for index, lista in camiseta_time.items():
                print("\nID:..................", index) 
                print("nome:..................", lista[0]) 
                print("time:..................", lista[1]) 
                print("tipo_produto:..................", lista[2]) 
                print("descrição:..................", lista[3]) 
                print("valor:..................", lista[4]) 
                print("quantidade:..................", lista[5]) 
                print("material:..................", lista[6]) 
    elif escolha == 2:
        buscar = input("Entre com o nome do produto: ").title() 
        for index, lista in camiseta_time.items():
            if buscar == lista[0]:
                print("\nID:..................", index) 
                print("nome:..................", lista[0]) 
                print("time:    ''................", lista[1]) 
                print("tipo_produto:..................", lista[2]) 
                print("descrição:..................", lista[3]) 
                print("valor:..................", lista[4]) 
                print("quantidade:..................", lista[5]) 
                print("material:..................", lista[6])  
            else:
                print("Erro")
    else:
        print("Algo de errado não está certo")
busca()


    #elif escolha == "2":
    #    buscar = input("Entre com o nome do produto: ") 
    #        if buscar == camiseta_time[0]:
    #            for index, lista
    #else
##:
#nome
#time
#tipo_produto
#descrição
#valor
#quantidade
#material

