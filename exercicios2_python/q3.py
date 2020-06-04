# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:      F - Feminino, M - Masculino, Sexo Inválido.
s = input("Digite seu sexo: ")
f = "f"
m = "m"
if(s == f):
  print("Feminino")
elif(s == m):
  print("Masculino")
else:
  print("Sexo Inválido")