# Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:

# a) esse funcionário foi contratado em 2000, com salário inicial de R$1.000,00;
#
# b) Em 2001, ele recebeu aumento de 1,5%, sobre o seu salário inicial;
#
# c) A partir de 2002 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
#
# Faça um programa que determine o salário desse funcionário dos anos de 2000 à 2017. Apresente todos os valores.

Salario = 1000.00
AnoContratacao = 2000

for Ano in range(2000, 2018):
    print(f"Ano {Ano}: R$ {Salario:.2f}")

    if Ano >= 2001:
        AumentoPercentual = 1.5 if Ano == 2001 else AumentoPercentual * 2
        Salario += Salario * (AumentoPercentual / 100)

    AnoContratacao = Ano
