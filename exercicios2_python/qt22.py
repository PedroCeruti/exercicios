#Vide "Atividades.txt"
num = float(input("Digite um número: "))
if(num == round(num)):
  print("Inteiro")
else:
  print("Decimal")
  print("Arredondado para baixo: ",round(num-0.5))
  print("Arredondado para cima: ",round(num+0.5))