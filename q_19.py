mesada = 10

nota = input("tirou A em matematica? (s/n): ")

if nota == "s":
    mesada += 20
    print(f"parabens, vai ganhar R${mesada} de mesada")
else:
    print(f"patetico, toma {mesada} conto de consolo")