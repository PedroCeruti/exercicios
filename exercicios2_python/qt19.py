#Vide "Atividades.txt"
n = int(input("Digite um número: "))
if(n <= 1000):
  c = (n // 100)
  restoc = (n % 100)
  d = (restoc // 10)
  restod = (restoc % 10)
  u = (restod)
  print(f"{n} = {c} centena(s), {d} dezena(s) e {u} unidade(s) ")
else:
  print("Valor Inválido")