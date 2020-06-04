'''Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''

hrs = float(input("Digite as horas trabalhadas: "))
ganho = float(input("Digite o valor ganho por hora: "))
s = hrs*ganho
print(f"Salário: {s}")
