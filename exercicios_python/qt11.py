peso = float(input("Peso de peixes: "))
excesso = (peso - 50)
multa = (excesso * 4)
if(peso > 50):
  print("O excesso foi de {:.2f} Kg".format(excesso))
  print("A multa à pagar será de R${:.2f}".format(multa))
elif(peso <= 50):
  print("Carga OK")