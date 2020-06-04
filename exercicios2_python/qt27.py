'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                              Até 5 Kg           Acima de 5 Kg
        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
  Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''
  
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