ano = int(input("digite um ano: "))

if ano <= 1500:
    print("voce encontrou os dinossauros")
elif ano > 1500 and ano < 2000:
    print("voce esta no seculo passado")
elif ano >= 2000 and ano <= 2026:
    print("voce esta no presente")
else:
    print("voce esta no futuro")