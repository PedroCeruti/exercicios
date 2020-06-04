''' As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5% 
  Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.'''
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