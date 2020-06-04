'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''
    
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