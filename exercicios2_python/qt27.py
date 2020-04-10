#Vide "Atividades.txt"
tp = input("Tipo de Carne: ")
qtde = float(input("Digite a quantidade em kilos(Kg): "))
pgto = input("Forma de Pagamento: ")
carnes = ["File Duplo", "Alcatra", "Picanha"]
if(tp in carnes):
  print(f"\nTipo da carne: {tp}")
  print(f"Quantidade de carne: {qtde}Kg")
  if(tp == "File Duplo"):
    if(qtde <= 5):
      v = (qtde * 4.9)
      print(f"\nValor total: R${v:.2f}")
    if(qtde > 5):
      v = (qtde * 5.8)
      print(f"\nValor total: R${v:.2f}")
  if(tp == "Alcatra"):
    if(qtde <= 5):
      v = (qtde * 5.9)
      print(f"\nValor total: R${v:.2f}")
    if(qtde > 5):
      v = (qtde * 6.8)
      print(f"\nValor total: R${v:.2f}")
  if(tp == "Picanha"):
    if(qtde <= 5):
      v = (qtde * 6.9)
      print(f"\nValor total: R${v:.2f}")
    if(qtde > 5):
      v = (qtde * 7.8)
      print(f"\nValor total: R${v:.2f}")
  print(f"Forma de Pagamento: {pgto}")
  if(pgto == "Dinheiro") or (pgto == "A vista"):
    print("Desconto: R$00.00")
    print(f"Total a pagar: R${v}")
  if(pgto == "Cartao"):
    desconto = v *(5/100)
    print(f"Valor do desconto: R${desconto:.2f}")
    vf = v - desconto
    print(f"Valor a pagar: R${vf:.2f}")
else:
  print("Esta carne não está em promoção")