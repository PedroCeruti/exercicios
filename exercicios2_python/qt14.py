#Vide "Atividades.txt"
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