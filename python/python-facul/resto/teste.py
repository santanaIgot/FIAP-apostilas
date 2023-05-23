qtd = int(input("Digite a quantidade de nota: "))
soma = 0

for nota in range(0, qtd):
    soma = soma + float(input("Digite a nota de número " + str(nota + 1) + ": "))

media = soma / qtd
print(media)
