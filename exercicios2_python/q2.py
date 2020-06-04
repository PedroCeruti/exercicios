#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.#
n1 = int(input("Digite um número: "))
if(n1 > 0):
  print("Positivo")
else:
  if(n1 == 0):
    print("Zero")
  else:
    print("Negativo")