#Vide "Atividades.txt"
num, num2 = input("Digite dois número: ").split()
num, num2 = float(num), float(num2)
op = input("Qual operação deseja realizar?\n")
operacoes = ["soma", "adição","+", "subtração","-", "multiplicação","x", "divisão","/","divisão inteira","//", "potência", "potenciação"]
if(op in operacoes):
  if(op == "soma") or (op =="adição") or (op == "+"):
    resultado = (num + num2)
    print("\nSoma:",resultado)
  elif(op == "subtração") or (op == "-"):
    resultado = (num - num2)
    print("\nSubtração:",resultado)
  elif(op == "multiplicação") or (op == "x"):
    resultado = (num*num2)
    print("\nMultiplicação:",resultado)
  elif(op == "divisão") or (op == "/"):
    resultado = (num/num2)
    print("\nDivisão:",resultado)
  elif(op == "divisão inteira") or ("//"):
    resultado = (num//num2)
    print("\nDivisão Inteira:",resultado)
  elif(op == "potência") or (op == "potenciação"):
    resultado = (num**num2)
    print("\nPotenciação:",resultado)
  if(resultado % 2 == 0):
    print("Par")
  else:
    print("Impar")
  if(resultado > 0):
    print("Positivo")
  elif(resultado == 0):
    print("Zero")
  else:
    print("Negativo")
  if(resultado == round(resultado)):
    print("Inteiro")
  else:
    print("Decimal")
else:
  print("Operação Inválida")