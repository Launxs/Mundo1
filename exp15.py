#advinhando um numero
import random
num = [0, 1, 2, 3, 4, 5]
ale = random.choice(num)
n = int(input("Estou pensando em um numero entre 0 e 5, tente advinhar: "))
if (n==ale):
    print("Paraben! voce acertou! >-<")
else:
    print("Que pena você errou ;-;")