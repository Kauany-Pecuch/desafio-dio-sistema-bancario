import textwrap
from datetime import date

def menu(): 
    menu = ("""\n
    ------------- Menu -------------
    1 - Cadastrar Usuário    
    2 - Criar Conta
    3 - Listar Contas            
    4 - Depositar
    5 - Sacar 
    6 - Visualizar Extrato
    0 - Sair
    -------------------------------- \n
                 
    Digite a opção que deseja: """)
       
    return input(textwrap.dedent(menu))

def validar_usuario(cpf, usuarios):
    existentes = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
    return existentes[0] if existentes else None 


def cadastrar_usuario(usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existe!")
        return
    
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (dia-mês-ano): ")
    endereco = input("Digite seu endereço((ogradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não existe!")

    
def listar_contas(contas):
    for conta in contas:
        cada_conta = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(cada_conta))



def depositar(valor_deposito, saldo, extrato,/):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito} - {date.today()}\n"
        print("Depósito realizado com sucesso!")

    else: 
        print("Valor informado inválido! Tente novamente.")

    return saldo, extrato
    
def sacar(*,saldo, valor_saque, extrato, MAXIMO_SAQUES, saques_dia, LIMITE_SAQUE):

    passou_saldo = valor_saque > saldo
    passou_limite = valor_saque > MAXIMO_SAQUES
    passou_maximo = date.today() == saques_dia >= LIMITE_SAQUE

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

    return saldo, extrato 

def visualizar_extrato(saldo,/, *, extrato):
    print("-----------------EXTRATO-----------------")
    print("Não houve movimentações em sua conta!" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("-----------------------------------------")


def main():

    saldo = 0
    extrato = ""
    saques_dia = 0
    LIMITE_SAQUE = 3
    MAXIMO_SAQUES = 500
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        operacao = menu()

        if operacao == "1":
            cadastrar_usuario(usuarios)
        
        elif operacao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif operacao == "3":
            listar_contas(contas)

        elif operacao == "4":
            valor_deposito = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(valor_deposito, saldo, extrato)

        elif operacao == "5":
            valor_saque = float(input("Digite valor do saque: "))

            saldo, extrato = sacar(
                 saldo = saldo,
                 valor_saque = valor_saque, 
                 extrato = extrato , 
                 MAXIMO_SAQUES = MAXIMO_SAQUES, 
                 saques_dia = saques_dia, 
                 LIMITE_SAQUE = LIMITE_SAQUE)

        elif operacao == "6":
            visualizar_extrato(saldo, extrato = extrato)
        
        elif operacao == "0":
            break

        else:
            print("Operação Inválida!")

main()