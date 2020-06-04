'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
  Álcool:
  até 20 litros, desconto de 3% por litro
  acima de 20 litros, desconto de 5% por litro
  Gasolina:
  até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''
    
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