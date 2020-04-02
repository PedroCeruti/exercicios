#Vide "Atividades.txt"
s = float(input("Digite o salário do colaborador: "))
if(s <= 280):
  percentual = "20%"
  aumento = s * (20/100)
  sa = (s + aumento)
elif(s >= 281) and (s <= 700):
  percentual = "15%"
  aumento = s * (15/100)
  sa = (s + aumento)
elif(s >= 701) and (s <= 1500):
  percentual = "10%"
  aumento = s * (10/100)
  sa = (s + aumento)
else:
  percentual = "5%"
  aumento = s * (5/100)
  sa = (s + aumento)
print(f"Salário antes do reajuste: R${s:.2f}")
print(f"Percentual aplicado: {percentual}")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Salário após reajuste: R${sa:.2f}")