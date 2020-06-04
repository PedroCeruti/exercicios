''' Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média
  A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E'''
n1, n2 = input("Digite as notas: ").split()
n1, n2 = float(n1), float(n2)
m = (n1 + n2)/2
print(f"\nNotas: {n1}, {n2}")
print(f"Média: {m}")
if(m <= 4) and (m >= 0):
  print("Conceito E")
  print("REPROVADO")
elif(m > 4) and (m <= 6):
  print("Conceito D")
  print("REPROVADO")
elif(m > 6) and (m <= 7.5):
  print("Conceito C")
  print("APROVADO")
elif(m > 7.5) and (m <= 9):
  print("Conceito B")
  print("APROVADO")
elif(m > 9) and (m <= 10):
  print("Conceito A")
  print("APROVADO")
else:
  print("Valores inválidos")