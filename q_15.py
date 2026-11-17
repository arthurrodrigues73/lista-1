passe = "lule"

senha = input("digite sua senha: ")

if senha == passe:
    print("acesso liberado")
elif senha == "LULE":
    print("quase la, mas voce GRITOU A SENHA!")
else:
    print("acesso negado")