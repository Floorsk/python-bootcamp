import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

agency = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
users = []
accounts = []

def saldo_value():
    return print(f"Seu saldo atual é: {saldo:.2f}")

def cpf_exists(cpf):
    if len(users) > 0:
        for i in users:
            if i["cpf"] == cpf:
                return True

def create_user(cpf):
    
    if cpf_exists(cpf): return print("Usuário já existe")
    
    name = input("Informe o nome do usuário: ")
    birthday_date = input("Informe sua data de nascimento: ")
    users.append({"cpf": cpf, "birthday_date": birthday_date, "name": name})

def create_account(cpf):
    
    if cpf_exists(cpf) == False: return print("É necessário criar um usuário para abri uma conta!")
    accounts.append({"agency": agency, "account": len(accounts) + 1, "cpf": cpf})

def list_accounts():
    print("--------------------------------------")
    for i in accounts:
        print(f"agência: {i["agency"]}")
        print(f"cpf: {i["cpf"]}")
        print(f"conta: {i["account"]}")
    print("--------------------------------------")
                
def list_users():
    print("--------------------------------------")
    for i in users:
        print(i["name"])
        print(i["cpf"])
        print(i["birthday_date"])
    print("--------------------------------------")
            
while True:
    opcao = menu()

    if opcao == "d":
        saldo += float(input("Valor para depositar: "))
        saldo_value()
    elif opcao == "s":
        saldo_value()
        while True:
            saque_value = float(input("Selecione valor do saque: "))
            if (saldo > saque_value):
                saldo -= saque_value
                extrato += f"\n Saque de {saque_value:.2f}"
                break
            else:
                print('Saldo insuficiente')
    elif opcao == "e":
        print(extrato)
    elif opcao == "nu":
        create_user(input("Informe o cpf: "))
    elif opcao == "lc":
        list_accounts()
    elif opcao == "nc":
        create_account(input("Informe o cpf: "))
    elif opcao == "q":
        break
    else:
        print("Essa opção não existe.")
