#Programa para calcular tempo de download#
#Vide "Atividades.txt"
tamanho = float(input("Digite o tamanho do arquivo (MB): "))
velocidade = float(input("Digite a velocidade do link (MBps): "))

t = (tamanho/velocidade)
m = (t * 60)/60
print(f"{m} minutos")