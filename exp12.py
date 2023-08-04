#hipotenusa
o = float(input("Digite o valor do cateto oposto: "))
a = float(input("Digite o valor do cateto adjacente: "))
h = ((o**2 + a**2)**0.5)
print (f"o valor da hipotenusa é de {h:.2f}")

#com biblioteca math
import math
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hi = math.hypot(co, ca)
print (f"o valor da hipotenusa é de {hi:.2f}")
