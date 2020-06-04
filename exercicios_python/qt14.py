'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        comprar apenas latas de 18 litros;
        comprar apenas galões de 3,6 litros;
        misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

m2 = float(input("Digite o tamanho da área a ser pintada: "))

l = m2/6
la = l/18
g = l/3.6
qtdel = 0
v = la * 80
print(f"Vão ser necessarias {la:.1f} latas")
print(f"Valor total: R${v:.2f} \n")
vg = g * 25
print(f"Vão ser necessarias {g} galões")
print(f"Valor total: R${vg:.2f} \n")
'''
if((l >= 3.6) and (l <= 17) or (l >= 18)):
  if(la != 0):
    qtdel += 1
  vt = v + vg
  print(f"Vão ser necessários {g} galões e {qtdel} latas")
  print(f"Valor total: R${vt:.2f}")
'''
