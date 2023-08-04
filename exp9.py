#faça um programa que leia um numero qualquer calcule e mostre a sua tabuada
a = int(input("Até qual numero ele deve calcular? "))
b = a+1
y = int(input("Informe o numero que seja saber a tabuada de 0 até {} dele: ".format(b)))
print("digite 1 para multiplicação")
print("digite 2 para subtração")
print("digite 3 para adição")
print("digite 4 para divisão")
z = int(input("informe um numero para o que vc deseja:"))
print(15*"-")
for x in range(b):
    if(z==1):
        print(f"{y} x {x} = {y*x}")
    elif(z==2):
        print(f"{y} - {x} = {y-x}")
    elif(z==3):
        print(f"{y} + {x} = {y+x}")
    elif(z==4):
        print(f"{y} / {x} = {y/x}")
    else:
        print("Aconteceu um erro")
print(15*"-")
