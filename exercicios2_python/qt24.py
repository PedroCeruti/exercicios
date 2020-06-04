'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?" 
      O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''
      
qtde1, qtde2, qtde3, qtde4, qtde5 = 0, 0, 0, 0, 0
resposta1 = input("Telefonou para a vitima?\n")
if(resposta1 == "sim") or (resposta1 == "Sim"):
  qtde1 += 1
resposta2 = input("Esteve no local do crime?\n")
if(resposta2 == "sim") or (resposta2 == "Sim"):
  qtde2+=1
resposta3 = input("Mora perto da vitíma?\n")
if(resposta3 == "sim") or (resposta3 == "Sim"):
  qtde3+=1
resposta4 = input("Devia para a vitima?\n")
if(resposta4 == "sim") or (resposta4 == "Sim"):
  qtde4+=1
resposta5 = input("Já trabalhou com a vitíma?\n")
if(resposta5 == "sim") or (resposta5 == "Sim"):
  qtde5 += 1
qtde = (qtde1 + qtde2 + qtde3 + qtde4 + qtde5)
if(qtde == 0):
  print("\nInocente")
if(qtde == 2):
  print("\nSuspeito")
if(qtde >= 3) and (qtde <= 4):
  print("\nCumplice")
if(qtde == 5):
  print("\nAssasino")