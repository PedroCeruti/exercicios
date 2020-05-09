#Vide "Atividades.txt"
while True: 
  a = int(input("Digite a população do país 'A': "))
  while(a <= 0):
    a = int(input("Digite a população do país 'A': "))
  b = int(input("Digite a população do país 'B': "))
  while(b <= 0):
    b = int(input("Digite a população do país 'B': "))
  taxa_a = int(input("Digite a taxa de crescimento de 'A'(%): "))
  while(taxa_a <= 0):
    taxa_a = int(input("Digite a taxa de crescimento de 'A'(%): "))
  taxa_b = int(input("Digite a taxa de crescimento de 'B'(%): "))
  while(taxa_b <= 0):
    taxa_b = int(input("Digite a taxa de crescimento de 'B'(%): "))
  ano = 0
  while(a < b):
    a += a * (taxa_a/100)
    b += b * (taxa_b/100)
    ano += 1
  print(f"'A' ultrapassa ou se iguala a 'B' em {ano} anos\n")