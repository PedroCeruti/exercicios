#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
''' Série de Fibonacci '''

n = int(input("Digite o termo a ser encontrado: "))
a = 1
p = 1
if (n == 1) or (n == 2):
  print("1")
else:
  count = 3
  while (count <= n):
    termo = (a + p)
    a = p
    p = termo
    count += 1 
    print(termo)