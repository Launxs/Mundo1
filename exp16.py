#multar um carro por limite de velocidade
vel = int(input("Qual foi a velocidade do carro em km/h? "))
if (vel > 80):
    diferenca = (vel-80)
    multa = float(diferenca*7)
    print("Você estava dirigindo acima do limite de 80km/h e por isso vai ser multado")
    print("A multa é de R$ 7,00 por cada km/h acima do limite")
    print (f"sua multa foi de R$ {multa:.2f}")
else:
    if (vel == 80):
        print("Você está dirigindo no limite de velocidade tenha mais cuidado para não ultrapassar")
    else:
        print("Tudo certo")