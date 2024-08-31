saldo = 0
numero_de_saques = 0
extrato = ""
LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUES = 3

def print_menu():
    print(f"""\n{" MENU ".center(20, "=")}
[d] => Depositar
[s] => Sacar
[e] => Ver Extrato
[q] => Sair
{"".center(20, "=")}
"""
)
    
def depositar():
    valor_deposito = float(input("Qual valor vai depositar? "))
    global saldo
    saldo += valor_deposito
    global extrato
    extrato += f"\nDepósito: R$ {valor_deposito:.2f}"
    print(f"R$ {valor_deposito:.2f} depositado com sucesso!")

def sacar():
    global saldo
    global extrato
    global numero_de_saques
    if numero_de_saques >= LIMITE_SAQUES:
        print("Limite de saques atingido!")
    else:
        valor_saque = float(input("Quanto deseja sacar? "))
        if valor_saque > saldo:
            print(f"Valor de saque maior que o saldo! Saldo: R$:{saldo:.2f}")
        elif valor_saque > LIMITE_VALOR_SAQUE:
            print(f"Valor de saque maior que o limite de R$ {LIMITE_VALOR_SAQUE:.2f}")
        else:
            saldo -= valor_saque
            extrato += f"\nSaque: R$ {valor_saque:.2f}"
            numero_de_saques += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

def ver_extrato():
    global extrato
    global saldo
    print(f"""{" EXTRATO ".center(20, "=")}{extrato}
\nSaldo R$ {saldo:.2f}
{"".center(20, "=")}
"""
)    

while True:
    print_menu()
    operacao = input("Qual a sua operação? ")

    if operacao == "d":
        depositar()
    elif operacao == "s":
        sacar()
    elif operacao == "e":
        ver_extrato()
    elif operacao == "q":
        print("Obrigado por usar nossos serviços! Até mais!")
        break
    else:
        print("Comando Inválido! Tente novamente")