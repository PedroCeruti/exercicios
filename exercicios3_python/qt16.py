#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
''' Série de Fibonacci '''
a = 1
p = 1
while True:
  termo = (a + p)
  a = p
  p = termo 
  print(termo)
  if (termo > 500):
    break