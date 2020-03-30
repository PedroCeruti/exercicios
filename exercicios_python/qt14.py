m2 = float(input("Digite o tamanho da área a ser pintada: "))

l = m2/6
la = l/18
g = l/3.6
if(l >= 18):
  v = la * 80
  print(f"Vão ser necessarias {la} latas")
  print(f"Valor total: R${v:.2f}")
if(l >= 3.6) and (l <= 17):
  vg = g * 25
  print(f"Vão ser necessarias {g} galões")
  print(f"Valor total: R${vg:.2f}")