from inventariop import *

produtos = {1:["Banana",20,3,12345,1.0,"18/03/2023","",1,"Copa","São Paulo"], 3:["Notebook",2,-1,54321,3500.0,"01/01/2023","",3000,"RH","São Paulo"]}

while True:
    print("Bem vindo:\n")
    print("Digite 1 para adicionar;")
    print("Digite 2 para relatório;")
    print("Digite 3 para busca simples;")
    print("Digite 4 para busca por nome;")
    print("Digite 5 para alterar quantidade;")
    print("Digite 6 para remover por ID;")
    print("Digite 7 para remover por nome;")
    print("Digite 8 para sair;")
    opcao = int(input("Entre com a opção desejada: "))

if opcao == 1:
    adicionar()
elif opcao == 2:
    relatorio()
elif opcao == 3:
    buscar_simples()
elif opcao == 4:
    buscar()
elif opcao == 5:
    alterar()
elif opcao == 6:
    remover_por_index()
elif opcao == 7:
    remover()
elif opcao == 8:
    quit()

