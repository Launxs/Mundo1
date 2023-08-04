n1 = int(input('Informe um numero:'))
n2 = int(input('Informe outro numero:'))
s = n1+n2
t = n1-n2
u = n1*n2
v = n1/n2
w = n1//n2
x = n1%n2
y = n1**n2
# Ordem de precedência
# Primeiro vem os parenteses ()
# Depois vem a potencia **
# Depois vem * , /, // e %
# E por fim vem + e -
print(f"A soma do número {n1} com o número {n2} é: {s}")
print(f"A subtrção do número {n1} com o número {n2} é: {t}")
print(f"A multiplicação do número {n1} com o número {n2} é: {u}")
print(f"A divisao do número {n1} com o número {n2} é: {v}")
print(f"A divisão inteira do número {n1} e do número {n2} é: {w}")
print(f"O resto da divisão do número {n1} com o número {n2} é: {x}")
print(f"O número {n1} elevado ao {n2} é: {y}")