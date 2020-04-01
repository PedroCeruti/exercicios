#Vide "Atividades.txt"
n1, n2, n3 = input("Digite 3 números: ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if(n3 > n2) and (n3 > n1):
  if(n2 > n1):
    print(n3, n2, n1)
  else:
      print(n3, n1, n2)