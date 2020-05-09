#Vide "Atividades.txt"
nome = ""
idade = 0
salario = 0
sexo = ""
estado_civil = ""
while(len(nome)<= 3):
  print("Nome inválido")
  nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
while(idade <= 0) or (idade > 150):
  idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
while(salario <= 0):
  salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo: ")
while(sexo != "f") and (sexo != "m"):
  sexo = input("Digite seu sexo: ")
estado_civil = input("igite seu estado civil: ")
while(estado_civil != "s") and (estado_civil != "c") and (estado_civil != "v") and (estado_civil != "d"):
  estado_civil = input("Digite seu estado civil: ")