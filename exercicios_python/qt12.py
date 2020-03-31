#Programa para calcular o salário#
#Vide "Atividades.txt"
hrs = float(input("Digite as horas trabalhadas: "))
ganho = float(input("Digite o valor ganho por hora: "))

sb = (hrs * ganho)
ir = (sb * 11/100)
inss = (sb * 8/100)
sindicato = (sb * 5/100)
descontos = (ir + inss + sindicato)
sl = (sb - descontos)

print(f"Sálario bruto: R${sb:.2f}")
print(f"Desconto do Imposto de Renda: R${ir:.2f}")
print(f"Desconto do INSS: R${inss:.2f}")
print(f"Desconto do Sindicato: R${sindicato:.2f}")
print(f"Salário liquido: R${sl:.2f}")