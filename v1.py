from datetime import date

menu = """
------------- Menu -------------
                 
1 - Depositar
2 - Sacar 
3 - Visualizar Extrato
0 - Sair
--------------------------------
                 
Digite a opção que deseja: """

saldo = 0
extrato = ""
saques_dia = 0
LIMITE_SAQUE = 3
MAXIMO_SAQUES = 500


while True:

    operacao = input(menu)

    if operacao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito} - {date.today()}\n"
            print("Depósito realizado com sucesso!")

        else: 
            print("Valor informado inválido! Tente novamente.")

    elif operacao == "2":
        valor_saque = float(input("Digite valor do saque: "))

        passou_saldo = valor_saque > saldo
        passou_limite = valor_saque > MAXIMO_SAQUES
        passou_maximo = date.today() == date.today() and saques_dia >= LIMITE_SAQUE

        if passou_saldo: 
            print("Valor de saque maior que saldo na conta. Não é possível realizar saque")

        elif passou_limite:
            print("O valor máximo de saque é R$ 500. Não foi possível realizar saque!")

        elif passou_maximo:
            print("Limite de saques por dia é de 3 saques. Não foi possível de realizar saque!")

        elif valor_saque > 0:
            saques_dia += 1
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque} - {date.today()}\n"
            print("Saque realizado com sucesso!")

        else:
            print("Valor inválido!")

    elif operacao == "3":
        print("-----------------EXTRATO-----------------")
        print("Não houve movimentações em sua conta!" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("-----------------------------------------")
        
    elif operacao == "0":
        break

    else:
        print("Operação Inválida!")
