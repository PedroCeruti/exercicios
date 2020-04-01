#Vide "Atividades.txt"
p1 = float(input("Digite o valor do primeiro protudo: "))
p2 = float(input("Digite o valor do segundo protudo: "))
p3 = float(input("Digite o valor do terceiro protudo: "))

if(p1 < p2) and (p1 < p3):
  print("O produto a ser comprado é o primeiro")
elif(p2 < p3) and (p2 < p1):
  print("O produto a ser comprado é o segundo")
else:
  print("O produto a ser comprado é o terceiro")