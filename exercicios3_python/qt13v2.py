#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite o valor da Base: "))
expoente = int(input("Digite o valor do Expoente: "))
potencia = 1
qtde = 1
while qtde <= expoente:
  potencia *= base
  qtde += 1
print(base, "^", expoente, "=", potencia)