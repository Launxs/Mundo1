salario = float(input("Digite o valor do salário: "))
if salario > 1250.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
novo_salario = salario + aumento
print("O valor do aumento é de R$", aumento)
print("O novo salário é de R$", novo_salario)
