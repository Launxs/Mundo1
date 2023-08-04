#distancia entre cidades
dis = int(input("Qual a distancia em km entre as cidadades que voce deseja viajar? "))
x = 0.45
y = 0.5
if (dis>200):
    valor = float(dis*x)
    print (f"O preço da passagem vai ser de: R${valor}")
else:
    valor = float(dis*y)
    print (f"O preço da passagem vai ser de: R${valor}")