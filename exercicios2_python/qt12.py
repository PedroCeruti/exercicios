#Vide "Atividades.txt"
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