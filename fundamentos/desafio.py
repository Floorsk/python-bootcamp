menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def saldo_value():
    return print(f"Seu saldo atual é: {saldo:.2f}")

while True:

    opcao = input(menu)

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
    elif opcao == "q":
        break
    else:
        print("Essa opção não existe.")
