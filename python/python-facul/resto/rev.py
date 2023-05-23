##Revisão(Cp)

#Calcular uma Média simple
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
media = (numero1 + numero2) / 2
print("A média é igual a:", str(media))

def calcular_media(numero1, numero2):
    #Calcular uma media simples
    media = (numero1 + numero2)/2

    print("A media é igual a:" + str(media))

resp = "S"
while resp == "S":
    nota1 = float(input("Digite o primeiro Numero: "))
    nota2 = float(input("Digite o segundo Numero: "))

    calcular_media(nota1, nota2)
    resp = input("Desejo continuar?(S ou N) ").upper()