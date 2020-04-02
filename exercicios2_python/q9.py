#Vide "Atividades.txt"
n1, n2, n3 = input("Digite 3 números: ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if(n3 > n2) and (n3 > n1):
  if(n2 > n1):
    print(n3, n2, n1)
  else:
      print(n3, n1, n2)
elif(n2 > n3) and (n2 > n1):
  if(n1 > n3):
    print(n2, n1, n3)
  else:
    print(n2, n3, n1)
else:
  if(n1 > n2) and (n2 > n3):
    print(n1, n2, n3)
  else:
    print(n1, n3, n2)