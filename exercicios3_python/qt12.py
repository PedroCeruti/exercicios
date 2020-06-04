#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

n = int(input("Valor da Tabuada: "))
for i in range(1, 11):
  v = (n * i)
  print(f"{n} x {i} = {v}")