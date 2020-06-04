#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = 0
impar = 0
for i in range(10):
  n = int(input("Digite um número: "))
  if (n % 2 == 0):
    par += 1
  else:
    impar += 1
print("Quantidade de números pares: ",par)
print("Quantidade de números impares: ",impar)