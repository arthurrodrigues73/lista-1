range = input("prefere atacar de longe (a) ou de perto(b)?: ")

if range == "a":
    tiro =  input("prefe magia (a) ou arco (b)?: ")
    if tiro == "a":
        print("mago")
    else:
        print("arqueiro")
else:
    arma = input("prefere espada (a) ou adagas (b)?: ")
    if arma == "a":
        print("guerreiro")
    else:
        print("assassino")