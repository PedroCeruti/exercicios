#Programa para calcular latas e galões de tinta#
#Vide "Atividades.txt"
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