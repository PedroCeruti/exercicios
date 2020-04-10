#Vide "Atividades.txt"
l = float(input("\nDigite a quantidade de litros: "))
c = input("Combustível: ")
if(c == "A"):
  if(l <= 20):
    v = (l * 1.9)
    desconto = v * (3/100)
    total = v - desconto
    print(f"\nTotal: R${v}")
    print(f"Desconto de 3%")
    print(f"Desconto: R${desconto}")
    print(f"Valor Final: R${total}")
  if(l > 20):
    v = (l * 1.9)
    desconto = v * (5/100)
    total = v - desconto
    print(f"\nTotal: R${v}")
    print(f"Desconto de 5%")
    print(f"Desconto: R${desconto}")
    print(f"Valor Final: R${total}")
if(c == "G"):
  if(l <= 20):
    v = (l * 2.5)
    desconto = v * (4/100)
    total = v - desconto
    print(f"\nTotal: R${v}")
    print(f"Desconto de 4%")
    print(f"Desconto: R${desconto}")
    print(f"Valor Final: R${total}")
  if(l > 20):
    v = (l * 2.5)
    desconto = v * (6/100)
    total = v - desconto
    print(f"\nTotal: R${v}")
    print(f"Desconto de 6%")
    print(f"Desconto: R${desconto}")
    print(f"Valor Final: R${total}")