'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
  Desconto do IR:
  Salário Bruto até 900 (inclusive) - isento
  Salário Bruto até 1500 (inclusive) - desconto de 5%
  Salário Bruto até 2500 (inclusive) - desconto de 10%'''
hrs = float(input("Digite as horas trabalhadas: "))
ganho = float(input("Digite o valor ganho por hora: "))

sb = (hrs * ganho)
inss = (sb * 10/100)
sindicato = (sb * 3/100)
fgts = (sb * 11/100)

if(sb <= 900):
  ir = 0
elif(sb <= 1500):
  ir = (sb * 5/100)
elif(sb <= 2500):
  ir = (sb * 10/100)
elif(sb > 2500):
  ir = (sb * 20/100)

descontos = (ir + inss)
sl = (sb - descontos)
print(f"\nSálario bruto: R${sb:.2f}")
print(f"Desconto do Imposto de Renda: R${ir:.2f}")
print(f"Desconto do INSS: R${inss:.2f}")
print(f"FGTS: R${fgts:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(f"Total de descontos: R${descontos:.2f}")
print(f"Salário liquido: R${sl:.2f}")