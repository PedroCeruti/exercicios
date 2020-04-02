#Vide "Atividades.txt"
# ax2 + bx + c #
# Delta(d) = b**2 - 4*a*c #
# X =(-b abs(d**0.5))/2*a
a = int(input("Digite o valor de A: "))
if(a != 0):
  b = int(input("Digite o valor de B: "))
  c = int(input("Digite o valor de C: "))
  delta = (b**2) - 4*a*c
  x1 = (-b + (delta**0.5))/2*a
  x2 = (-b - (delta**0.5))/2*a
  if(delta < 0):
    print("\nA equação não possui raizes reais.")
  elif(delta == 0):
    print("\nA equação possui apenas uma raiz real")
    print(f"x = {x1}")
  else:
    print(f"\nA equação possui duas raizes reais \nx1 = {x1:.2f} \nx2 = {x2:.2f}")