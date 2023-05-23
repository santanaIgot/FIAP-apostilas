resp = "s"
qtd = 0
soma = 0

while resp == "s":
    soma = soma + float(input("Digite a nota de número " + str(qtd + 1)))
    qtd += 1
    resp = input("Deseja continuar?(S ou N)").upper()
    while resp != "S" and resp != "N":
        print("Resposta inválida.")
        resp = input("Deseja continuar?(S ou N)").upper()
    
media = soma / qtd
print(media) 