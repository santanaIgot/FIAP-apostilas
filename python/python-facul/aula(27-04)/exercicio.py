#Crie um dicionario com os dados de um usuario;
usuario = {1:["Gabriel", 18, "00.000.000-0", "aaa@gmail.com", "87687", "SP", "ADS"], 
           2:["Beatriz", 36, "00.000.000-1", "bbb@gmail.com", "84576", "RJ", "Coordenadora"], 
           3:["Elder", 38, "00.000.000-2", "ccc@gmail.com", "67576", "BA", "Personal Trainer"], 
           4:["Geovanna", 14, "00.000.000-3", "ddd@gmail.com", "98798", "SP", "Dsempregada"], 
           5:["Karina", 19, "00.000.000-4", "eee@gmail.com", "90809", "SP", "Enfermeira"],
           6:["Lupita", 4, "00.000.000-1", "fff@gmail.com", "987909", "SP", "Desempregada"]}

#Crie uma função que crie um novo usuario;
def adicionar():
    id = list(usuario.keys)
    usuario[id[len(id)-1]+1] = [input("Entre com o nome do usuário: "), 
                            int(input("Entre com a idade do usuário: ")), 
                                input("Entre com o RG do usuário: "), 
                                input("Entre com o email do usuário: "), 
                                input("Entre com a senha do usuário: "), 
                                input("Entre com o estado em que o usuário nasceu: "), 
                                input("Entre com a profissão do usuário: ")]

#Crie uma função que gerar o relatorio de usuarios.
def relatorio(): 
    for index, lista in usuario.items:
        print("n\ID:........................."), id[index],
        print("Nome:........................."), lista[0],
        print("Idade:........................."), lista[1],
        print("RG:........................."), lista[2],
        print("Email:........................."), lista[3],
        print("Senha:........................."), lista[4],
        print("Estado:........................."), lista[5],
        print("Profissão:........................."), lista[6],



