user = ["alberico", "pedro", "eduarda"]
senha = ["a1b2c3", "123456", "654321"]
input_user = input("entre com o nome do usuario: ").lower()
input_senha = input("entre com a senha do usuario: ").lower()
for index in range(0, len(user)):
    if (input_user == user[index]) and (input_senha == senha[index]):
        print("Sucesso!!!")
        quit()
print("Dados incorretos.")