#Vide "Atividades.txt"
n = int(input("Digite um valor: "))
if(n >= 10) and (n <= 600):
  c100 = (n // 100)
  resto100 = (n % 100)
  c50 = (resto100 // 50)
  resto50 = (resto100 % 50)
  c10 = (resto50 // 10)
  resto10 = (resto50 % 10)
  c5 = (resto10 // 5)
  resto5 = (resto10 % 5)
  c1 = resto5
  print(f"{c100} cédula(s) de R$100")
  print(f"{c50} cédula(s) de R$50")
  print(f"{c10} cédula(s) de R$10")
  print(f"{c5} cédula(s) de R$5")
  print(f"{c1} cédula(s) de R$1")
else:
  print("Valor para saque inválido")