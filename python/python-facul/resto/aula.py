#nome = input('Hello, What is your name? ')
#msg2 = int(input('Ok, {}. How old are you?'.format(nome)))

nome = "Gabriel"
idade = 23
pressao = 12.8
glicemia = 105
tiposSanguinio = 1

if idade >= 60 and pressao >= 13.10: 
    print("Partiu emergência!")
elif idade < 60 and pressao > 14.10:
    print("Emergência")
elif idade > 60 and pressao <= 12.8:
    print("Urgência")
elif idade < 60 and pressao <= 12.8:
    print("Vai para casa descansar")