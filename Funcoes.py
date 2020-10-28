class Formulario:
    peso1 = 0
    peso2 = 0
    peso3 = 0
    dica1 = ""
    dica2 = ""
    dica3 = ""

    def login(self):
        print("Digite seu email:\n")
        print("Digite sua senha:\n")
        print("\nCadastrar\n")
        email = input("")
        opcao = email.upper()
        if opcao == "CADASTRAR":
            print("\nCadastro\n")
            nome_u = input("Nome do usuário: ")
            email = input("\nEmail: ")
            senha = input("\nSenha: ")
            con_senha = input("\nConfirmar senha: ")
            if con_senha == senha:
                manipulador = open("Cadastro.txt", "a", encoding="utf8")
                manipulador.write(nome_u)
                manipulador.write("\n")
                manipulador.write(email)
                manipulador.write("\n")
                manipulador.write(senha)
                manipulador.write("\n")
                manipulador.close()
        elif opcao != "CADASTRAR":
            senha = input("")
            print("\n\n\n\n\n")

    def cadastrar_c(self):
        nome_c = input("\nNome: ")

        # A idade da criança estava atrapalhando o funcionamento do código, por isso optamos por deixa-la de fora no momento
        idade_c = input("\nIdade:")

        manipulador = open("Cadastros_crianças.txt", "a", encoding="utf8")
        manipulador.write(nome_c)
        manipulador.write("\n\n")
        manipulador.close()

    def pergunta_1(self):
        print("Você deixa que o seu filho/a utilize o fogão?\n>\n")
        opcao = input("")
        opcao = opcao.upper()
        if opcao == "SIM":
            self.peso1 = 0
            self.dica1 = "-Não deixe-a usar o fogão\n"
        elif opcao == "NÃO":
            self.peso1 = 31
            self.dica1 = ""

    def pergunta_2(self):
        print("\nVocê costuma deixar seus filhos/as sozinhos/as em casa?\n< >\n")
        opcao = input("")
        opcao = opcao.upper()
        if opcao == "SIM":
            self.peso2 = 0
            self.dica2 = "-Nunca deixe seus filhos/as sozinhos em casa\n"
        elif opcao == "NÃO":
            self.peso2 = 46
            self.dica2 = ""

    def pergunta_3(self):
        print("\nVocê deixa seu filho/a mexer com eletricidade\n< finalizar\n")
        opcao = input("")
        opcao = opcao.upper()
        if opcao == "SIM":
            self.peso3 = 0
            self.dica3 = "-Não permita que seu filho/a mexa em eletricidade\n"
        elif opcao == "NÃO":
            self.peso3 = 23
            self.dica3 = ""
