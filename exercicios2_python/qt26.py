#Vide "Atividades.txt"
kgmo = float(input("Digite o peso dos morangos: "))
kgm = float(input("Digite o peso das maçãs: "))
kg = (kgm + kgmo)
if(kgmo <= 5):
  v1 = (kgmo * 2.5)
if(kgmo > 5):
  v1 = (kgmo * 2.2)
if(kgm <= 5):
  v2 = (kgm * 1.8)
if(kgm > 5):
  v2 = (kgm * 1.5)
vt = (v1 + v2)
print(f"\nValor dos Morangos: R${v1:.2f}")
print(f"Valor das Maçãs: R${v2:.2f}")
print(f"Valor total: R${vt:.2f}")
if(kg > 8) or (vt > 25):
  desconto = vt * (10/100)
  vf = (vt - desconto)
  print(f"Desconto: R${desconto:.2f}")
  print(f"Valor Final: R${vf:.2f}")