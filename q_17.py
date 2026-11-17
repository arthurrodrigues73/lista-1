p_c = 10
p_m = 8
p_v = 6
conta = 0

print("à venda")
while True:
    print("\n1-poção de cura\n2-poção de mana\n3-poção de velocidade\n0-nada")
    action = int(input("o que quer comprar?: "))

    if action == 1:
        conta += 10
    elif action == 2:
        conta += 8
    elif action == 3:
        conta += 6
    elif action == 0:
        print(f"total: R${conta}")
        break
    else:
        print("\nação inválida")