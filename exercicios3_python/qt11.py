#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
s = 0
if(n1 >= n2):
  for i in range(n2, n1):
    print(i)
    s += i
  print(f"\n{s}")
elif(n2 > n1):
  for i in range(n1, n2):
    print(i)
    s += i
  print(f"\n{s}") 