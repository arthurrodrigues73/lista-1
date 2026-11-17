# senha = "qwerty"
# pin = 6769

nsenha = input("digite sua senha: ")

if nsenha == "qwerty":

    npin = int(input("digite seu pin: "))

    if npin == 6769:
        print("acesso liberado")
    else:
        print("acesso bloqueado")
else:
    print("acesso bloqueado")