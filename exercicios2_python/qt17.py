#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano: "))
if(ano % 4 == 0) or (ano % 400 == 0):
  print("É bissexto")
elif(ano % 100 != 0):
  print("Não bissexto")