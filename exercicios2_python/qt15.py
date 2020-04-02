#Vide "Atividades.txt"
l1 = float(input("Digite o 1º lado: "))
l2 = float(input("Digite o 2º lado: "))
l3 = float(input("Digite o 3º lado: "))
if(l1 + l2 > l3) or (l1 + l3 > l2) or (l2 + l3 > l1):
  if(l1 == l2 ==l3):
    print("Triângulo Equilátero")
  elif(l1 == l2) or (l2 == l3) or (l3 == l1):
    print("Triângulo Isósceles")
  elif(l1 != l2 != l3 != l1):
    print("Triângulo Escaleno")
else:
  print("Valores inválidos")