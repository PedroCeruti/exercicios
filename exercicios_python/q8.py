'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.'''

n1, n2, n3 = input("Digite 3 números: ").split()
n1, n2 = int(n1), int(n2)
n3 = float(n3)
a = ((n1 * 2) * (n2 / 2))
b = ((n1 * 3) + (n3))
c = (n3 ** 3)
print(a)
print(b)
print(c)
