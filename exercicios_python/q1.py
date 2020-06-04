#Programa que peça as 4 notas bimestrais e mostre a média.#
n1, n2, n3, n4 = input("Digite as notas: ").split()
n1, n2, n3, n4 = int(n1), int(n2), int(n3), int(n4)

media = (n1 + n2 + n3 + n4)/4
print(f"Média: {media}")
