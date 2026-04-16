def main():
    user = input("Cadastre o usuário: ")
    senha = input("Crie uma senha: ")


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


main()
