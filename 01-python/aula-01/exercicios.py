nome = "Bruno Cavinatto Bilatto"
idade = 25
profissao = "Gerente comercial"
salario = 6000

print("Me chamo, ", nome, "tenho", idade, "anos, sou", profissao, 
       "e ganho", salario)

salario_anual = salario * 12

print("Meu salario anual R$",salario_anual)

salario_mensal = salario_anual / 12

print("Meu salario mensal é R$", salario_mensal)

aumento = salario_mensal*0.1
novo_salario = aumento + salario_mensal

print("Meu novo salario é", novo_salario)

desconto = novo_salario * 0.08

salario_liquido = novo_salario - desconto

print("Meu salario liquido é", salario_liquido)


nome_usuario = input("Qual é seu nome? ")
salario_usuario = int(input("Qual seu salario? "))
percentual_aumento = int(input("Qual percentual de aumento voce recebeu? "))
percentual_aumento_decimal = percentual_aumento / 100
novo_salario_usuario = salario_usuario + (salario_usuario * percentual_aumento_decimal)

print("Ola", nome_usuario, "Seu novo salario é", novo_salario_usuario)

