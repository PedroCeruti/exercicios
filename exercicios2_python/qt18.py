#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
d, m, a = input("Digite a data no formato dd/mm/aaaa: ").split("/")
d, m, a = int(d), int(m), int(a)
if(1 <= d <= 31) and (1 <= m <= 12) and (a > 1000):
  print("Data válida")
else:
  print("Data inválida")