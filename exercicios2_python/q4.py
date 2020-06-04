#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ")
vogal = ["a","e","i","o","u"]
if(letra in vogal):
  print("Vogal")
else:
  print("Consoante")