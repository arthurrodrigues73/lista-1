ouro = int(input("quanto de ouro você tem?: "))

if ouro > 1000:
    tax = ouro * 0.1
    print(f"você deve {tax} de imposto ao rei")
else:
    print("isento de impostos")