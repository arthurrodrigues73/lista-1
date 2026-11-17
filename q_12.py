age = int(input("digite sua idade: "))

if age >= 14:
    print("bem vindo a equipe avançada!")
else:
    age = 18 - age
    print(f"faltam {age} anos para você entrar na equipe avançada")