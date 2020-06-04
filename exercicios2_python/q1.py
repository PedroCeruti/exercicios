#Faça um Programa que peça dois números e imprima o maior deles.#
n1, n2 = input("Digite 2 números: ").split()
n1, n2 = int(n1), int(n2)

if(n1 > n2):
  print(n1)
else:
  print(n2)