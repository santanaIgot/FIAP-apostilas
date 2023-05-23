nome=["Camiseta", "Short"]
preco = [49.9, 30]
qtd = [8, 9]

for index in range(0, len(nome)):
    if qtd[index] > 1:
        print("Eu tenho " + str(qtd[index]) + " " + nome[index] + "s de R$" + str(preco[index]))
    else:
        print("Eu tenho " + str(qtd[index]) + " " + nome[index] + " de R$" + str(preco[index]))
 