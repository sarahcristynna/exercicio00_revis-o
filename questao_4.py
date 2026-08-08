usuario = input("Dígite o nome de usúario ")
senha = input("Dígite uma senha ")

while senha==usuario:
    print("Erro! A senha não pode ser igual ao número de usúario")
    print("-----------------------------------------------------")
    usuario = input("Dígite o nome de usuario ")
    senha = input("Dígite uma senha ")

print ("Cadastro realizado com sucesso! ")



