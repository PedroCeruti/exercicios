#Vide "Atividades.txt"
user = input("Usuário: ")
senha = input("Senha: ")
while(user == senha):
  print("Erro")
  user = input("Usuário: ")
  senha = input("Senha: ")
else:
  print("Bem Vindo!")