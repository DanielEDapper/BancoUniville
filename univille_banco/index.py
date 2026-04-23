def main():
    user = input("Cadastre o usuário: ")
    senha = input("Crie uma senha: ")
    saldo = 131
    limite = 100


    while True:
        print("\n--- UNIVILLE Internet Banking ---")
        print("1 - Acessar")
        print("2 - Encerrar")

        escolha = int(input("\nEscolha uma opção: "))

        if escolha == 1:
            tentativas = 0

            while tentativas < 3:
                tentativas_disponiveis = 2 - tentativas
                usuario_digitado = input("\nUsuário: ")
                senha_digitada = input("Senha: ")

                if usuario_digitado == user and senha_digitada == senha:
                    print("\nAcesso permitido!")
                    menuInicial(saldo, limite)
                    break
                else:
                    print("\nUsuário ou senha incorretos!")
                    tentativas += 1
                    print(f"Número de tentativas: {tentativas_disponiveis}")

            if tentativas == 3:
                print("Acesso bloqueado!")

        elif escolha == 2:
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")

def menuInicial(saldo, limite):
    continuar = True

    while continuar:
        print("===================================")
        print("==   UNIVILLE Internet Banking   ==")
        print("===================================")
        print("==   1 - Consultar Saldo         ==")
        print("==   2 - Realizar Saque          ==")
        print("==   3 - Realizar Depósito       ==")
        print("==   4 - Consultar limite        ==")
        print("==   5 - Encerrar                ==")
        print("===================================")

        opcao = int(input("Digite a opção desejada: "))

        match opcao:
            case 1:
                menuSaldo(saldo)
                limparTela()
            case 2:
                saldo = menuSaque(saldo, limite)
                limparTela()
            case 3:
                saldo = menuDeposito(saldo)
                limparTela()
            case 4:
                menuLimite(limite)
                limparTela()
            case 5:
                menuRetornar()
                continuar = False

def menuSaldo(saldo):
    print("===================================")
    print("==             SALDO             ==")
    print("===================================")

    print("                                   ")
    print(f"Saldo: R$ {saldo:.2f}")

def menuSaque(saldo, limite):
    print("===================================")
    print("==             SAQUE             ==")
    print("===================================")

    valor = int(input("Digite o valor do saque: R$"))

    if valor <= 0:
      print("Valor inválido")
    elif valor <= (saldo + limite):
      saldo -= valor
      print("Saque realizado com sucesso")
      print(f"Saldo: R$ {saldo:.2f}")
    else:
      print("Saldo insuficiente")
    return saldo

def menuDeposito(saldo):
    print("===================================")
    print("==            DEPÓSITO           ==")
    print("===================================")

    valor = int(input("Digite o valor do depósito: R$"))

    if valor <= 0:
      print("Valor inválido")
    else:
      saldo += valor
      print("Depósito realizado com sucesso")
      print(f"Saldo: R$ {saldo:.2f}")
    return saldo

def menuLimite(limite):
    print("===================================")
    print("==         MOSTRAR LIMITE        ==")
    print("===================================")
    print(f"Limite: R$ {limite:.2f}")

def menuRetornar():
    print("Encerrar Sistema Solicitado")
def limparTela():
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")
    print("                                        ")

main()
