'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

m2 = float(input("Digite o tamanho da área a ser pintada: "))
l = m2/3
la = l/18
if(l >= 18):
  v = la * 80
  print(f"Vão ser necessarias {la} latas")
  print(f"Valor total: R${v:.2f}")
else:
  print("Não é necessário 1 lata")
  