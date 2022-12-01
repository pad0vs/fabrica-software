valor_hora = float(input("Digite o valor da hora: "))
qtd_hora = float(input("Digite a quantidade de horas trabalhadas: "))
salarioBruto = valor_hora*qtd_hora
if salarioBruto <= 900:
    sindicato = salarioBruto*0.03
    inss = salarioBruto*0.10
    fgts = salarioBruto*0.11
    salarioLiquido = salarioBruto - sindicato - inss
    print(f"Valor do Salário Bruto R$ {salarioBruto:.2f}")
    print(f"Valor do Sindicato     R$ {sindicato:.2f}")
    print(f"Valor do INSS          R$ {inss:.2f}\n")
    print(f"O valor do salário líquido é R$ {salarioLiquido:.2f}")
    print(f"O valor do FGTS depositado em conta é: R$ {fgts:.2f}")

elif salarioBruto > 900 and salarioBruto <=1500:
    ir = salarioBruto * 0.05
    sindicato = salarioBruto*0.03
    inss = salarioBruto*0.10
    fgts = salarioBruto*0.11
    salarioLiquido = salarioBruto - sindicato - inss -ir
    print(f"Valor do Salário Bruto R$ {salarioBruto:.2f}")
    print(f"Valor do Sindicato     R$ {sindicato:.2f}")
    print(f"Valor do IR            R$ {ir:.2f}")
    print(f"Valor do INSS          R$ {inss:.2f}\n")
    print(f"O valor do salário líquido é R$ {salarioLiquido:.2f}")
    print(f"O valor do FGTS depositado em conta é: R$ {fgts:.2f}")

elif salarioBruto > 1500 and salarioBruto <=2500:
    ir = salarioBruto * 0.10
    sindicato = salarioBruto*0.03
    inss = salarioBruto*0.10
    fgts = salarioBruto*0.11
    salarioLiquido = salarioBruto - sindicato - inss -ir
    print(f"Valor do Salário Bruto R$ {salarioBruto:.2f}")
    print(f"Valor do Sindicato     R$ {sindicato:.2f}")
    print(f"Valor do IR            R$ {ir:.2f}")
    print(f"Valor do INSS          R$ {inss:.2f}\n")
    print(f"O valor do salário líquido é R$ {salarioLiquido:.2f}")
    print(f"O valor do FGTS depositado em conta é: R$ {fgts:.2f}")

elif salarioBruto > 2500:
    ir = salarioBruto * 0.2
    sindicato = salarioBruto*0.03
    inss = salarioBruto*0.10
    fgts = salarioBruto*0.11
    salarioLiquido = salarioBruto - sindicato - inss -ir
    print(f"Valor do Salário Bruto R$ {salarioBruto:.2f}")
    print(f"Valor do Sindicato     R$ {sindicato:.2f}")
    print(f"Valor do IR            R$ {ir:.2f}")
    print(f"Valor do INSS          R$ {inss:.2f}\n")
    print(f"O valor do salário líquido é R$ {salarioLiquido:.2f}")
    print(f"O valor do FGTS depositado em conta é: R$ {fgts:.2f}")