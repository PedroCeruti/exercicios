#Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if(n1 > n2) and (n1 > n3):
  print(n1)
elif(n2 > n3) and (n2 > n1):
  print(n2)
else:
  print(n3)