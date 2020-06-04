'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                              Até 5 Kg           Acima de 5 Kg
        Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
        Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
  Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''
  
kgmo = float(input("Digite o peso dos morangos: "))
kgm = float(input("Digite o peso das maçãs: "))
kg = (kgm + kgmo)
if(kgmo <= 5):
  v1 = (kgmo * 2.5)
if(kgmo > 5):
  v1 = (kgmo * 2.2)
if(kgm <= 5):
  v2 = (kgm * 1.8)
if(kgm > 5):
  v2 = (kgm * 1.5)
vt = (v1 + v2)
print(f"\nValor dos Morangos: R${v1:.2f}")
print(f"Valor das Maçãs: R${v2:.2f}")
print(f"Valor total: R${vt:.2f}")
if(kg > 8) or (vt > 25):
  desconto = vt * (10/100)
  vf = (vt - desconto)
  print(f"Desconto: R${desconto:.2f}")
  print(f"Valor Final: R${vf:.2f}")