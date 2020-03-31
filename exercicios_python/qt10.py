#Programa para calcular peso ideal (por sexo)#
#Vide "Atividades.txt"
sexo = input("M ou F: ")
M, F = sexo, sexo
h = float(input("Digite sua altura: "))
if(sexo == M):
  p = (72.7*h) - 58
  print("Seu peso ideal é: {:.2f} Kg".format(p))
elif(sexo == F):
  p1 = (62.1*h) - 44.7
  print("Seu peso ideal é: {:.2f} Kg".format(p1))