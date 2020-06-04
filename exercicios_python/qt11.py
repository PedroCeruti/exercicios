'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

peso = float(input("Peso de peixes: "))
excesso = (peso - 50)
multa = (excesso * 4)
if(peso > 50):
  print("O excesso foi de {:.2f} Kg".format(excesso))
  print("A multa à pagar será de R${:.2f}".format(multa))
elif(peso <= 50):
  print("Carga OK")
  