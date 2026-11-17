money = int(input("quanto dinheiro voce tem?: "))
jogo = int(input("qual o valor do jogo?"))

if money > jogo:
    troco = money - jogo
    print(f"mais que suficiente! e sobrará {troco} de troco")
elif money == jogo:
    print("quantia exata!")
else:
    print("quantia insuficiente")