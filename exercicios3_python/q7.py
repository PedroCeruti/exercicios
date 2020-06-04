#Faça um programa que leia 5 números e informe o maior número.

n1 = int(input("Digite um número: "))
nuns = [n1]
for i in range(4):
  n = int(input("Digite um número: "))
  nuns.append(n)
print(max(nuns))