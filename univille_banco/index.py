def main():
    user = input("Cadastre o usuário: ")
    senha = input("Crie uma senha: ")
    saldo = 131


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
                    menuInicial(saldo)
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

def menuInicial(saldo):
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
            case 2:
                print("Realizar Saque Solicitado")
            case 3: 
                print("Realizar Depósito Solicitado")
            case 4:
                print("Consultar Limite Solicitado")
            case 5:
                print("Encerrar Sistema Solicitado")
                continuar = False

def menuSaldo(saldo):
    print("===================================")
    print("==             SALDO             ==")
    print("===================================")

    print("                                   ")
    print(f"Saldo: R$ {saldo:.2f}")

def menuSaque():
    print("Realizar Saque Solicitado")

def menuDeposito():
    print("Realizar Depósito Solicitado")

def menuLimite():
    print("Consultar Limite Solicitado")

def menuRetornar():
    print("Encerrar Sistema Solicitado")


main()
