#Vide "Atividades.txt"
a = 8000
b = 20000
ano = 0
while(a < b):
  a += a * 0.03
  b += b * 0.015
  ano += 1
print(f"'A' ultrapassa ou se iguala a 'B' em {ano} anos")