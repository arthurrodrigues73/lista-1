dinheiro = int(input("quanto dinheiro voce tem?: "))

print("1- lanche - R$15,00\n2- suco - R$8,00\n3- combo - R$20,00\n0- nada")
act = int(input("\no que deseja?: "))

if act == 1:
    if dinheiro >= 15:
        print("compra liberada")
    else:
        print("compra negada")
elif act == 2:
    if dinheiro >= 8:
        print("compra liberada")
    else:
        print("compra negada")
elif act == 3:
    if dinheiro >= 20:
        print("compra liberada")
    else:
        print("compra negada")
elif act == 0:
    print("pobre")