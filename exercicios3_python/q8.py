#Faça um programa que leia 5 números e informe a soma e a média dos números.
v = 0
for i in range(5):
  n = int(input("Digite um número: "))
  v += n
m = (v/5)
print(f"A soma é de: {v}")
print(f"A média é de: {m}")