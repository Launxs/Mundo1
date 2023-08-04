#seno, cosseno e tangente
#com biblioteca math
import math
ang = int(input('Ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print(
    f"Com o angulo de {ang}º obtemos os seguintes dados:"
    f"seno é de: {seno}"
    f"cosseno é de {cosseno}"
    f"tangente é de: {tangente}"
)
