'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
  - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
  - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
  - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
  - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
  
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