import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

from time import sleep

seconds = 2
i = 0

class Formulario:
        peso1 = 0
        peso2 = 0
        peso3 = 0
        peso4 = 0
        peso5 = 0
        peso6 = 0
        peso7 = 0
        dica2 = ""
        dica3 = ""
        dica4 = ""
        dica5 = ""
        dica6 = ""
        dica7 = ""
        email = ""
        senha = ""
        nome_u = ""
        opc = 0

        def login(self):
                self.opc = int(input("1 - Login\n2 - Cadastrar\n\nEscolha uma das opções acima: "))
                print("\nEspere 2 segundos")
                sleep(seconds)
                cls()
                if self.opc == 1:
                        self.email = input("\nDigite seu email: ")
                        self.senha = input("\nDigite sua senha: ")
                if self.opc == 2:
                        print("\nCadastro\n")
                        self.nome_u = input("Nome do usuário: ")
                        self.email = input("\nEmail: ")
                        self.senha = input("\nSenha: ")
                        con_senha = input("\nConfirmar senha: ")
                        if con_senha == self.senha:
                                manipulador = open("Cadastro.txt", "a", encoding="utf8")
                                manipulador.write(self.nome_u)
                                manipulador.write("\n")
                                manipulador.write(self.email)
                                manipulador.write("\n")
                                manipulador.write(self.senha)
                                manipulador.write("\n")
                                manipulador.close()

        def cadastrar_c(self):
                nome_c = input("\nNome: ")

                # A idade da criança estava atrapalhando o funcionamento do código, por isso optamos por deixa-la de fora no momento, porém no futuro nós queremos que a idade sirva para determinar o teste que será enviado para o pai/mãe
                idade_c = input("\nIdade:")

                manipulador = open("Cadastros_crianças.txt", "a", encoding="utf8")
                manipulador.write(self.email)
                manipulador.write("\n")
                manipulador.write(nome_c)
                manipulador.write("\n\n")
                manipulador.close()

        def pergunta_1(self):
                print("Você tem mais de um filho(a) menor de 12 anos em casa?\n>\n")
                opcao = input("")
                opcao = opcao.upper()
                if opcao == "SIM":
                        self.peso1 = 0
                elif opcao == "NÃO":
                        self.peso1 = 1

        def pergunta_2(self):
                print("\nNormalmente seu filho(a) utilize o fogão sozinho?\n< >\n")
                opcao = input("")
                opcao = opcao.upper()
                if opcao == "SIM":
                        if self.peso1 == 0:
                                self.peso2 = 16
                        elif self.peso1 == 1:
                                self.peso2 = 18
                        self.dica2 = "-Não deixo-o(a) utilizar o fogão\n"
                elif opcao == "NÃO":
                        self.peso2 = 0
                        self.dica2 = ""

        def pergunta_3(self):
                print("\nVocê costuma deixar seu filho(a) sozinho(a)?\n< >\n")
                opcao = input("")
                opcao = opcao.upper()
                if opcao == "SIM":
                        if self.peso1 == 0:
                                self.peso3 = 20 
                        elif self.peso1 == 1:
                                self.peso3 = 16
                        self.dica3 = "-Sempre deixe alguem supervisionando-o(a)\n"
                elif opcao == "NÃO":
                        self.peso3 = 0
                        self.dica3 = ""

        def pergunta_4(self):
                print("\nSeu filho(a) normalmente mexe em eletricidade?\n< >\n")
                opcao = input("")
                opcao = opcao.upper()
                if opcao == "SIM":
                        if self.peso1 == 0:
                                self.peso4 = 16 
                        elif self.peso1 == 1:
                                self.peso4 = 18
                        self.dica4 = "-Não permita que seu filho/a mexa em eletricidade\n"
                elif opcao == "NÃO":
                        self.peso4 = 0
                        self.dica4 = ""

        def pergunta_5(self):
                print("\nVocê costuma avisar ao seu filho sobre os locais que estão molhados dentro de casa?\n< >\n")
                opcao = input("")
                opcao = opcao.upper()
                if opcao == "SIM":
                        self.peso5 = 0
                        self.dica5 = ""
                elif opcao == "NÃO":
                        if self.peso1 == 0:
                                self.peso5 = 12
                        elif self.peso1 == 1:
                                self.peso5 = 13
                        self.dica5 = "-Sempre avise o seu filho(a) que o piso está molhado\n"

        def pergunta_6(self):
                print("\nVocê permite que seu filho(a) utilize faca? \n< >\n")
                opcao = input("")
                opcao = opcao.upper()
                if opcao == "SIM":
                        if self.peso1 == 0:
                                self.peso6 = 21
                        elif self.peso1 == 1:
                                self.peso6 = 19
                        self.dica6 = "-Não permita que seu filho(a) utilize faca\n"
                elif opcao == "NÃO":
                        self.peso6 = 0
                        self.dica6 = ""

        def pergunta_7(self):
                print("\nVocê costuma deixar produtos de limpeza em locais de fácil acesso?\n< finalizar\n")
                opcao = input("")
                opcao = opcao.upper()
                if opcao == "SIM":
                        if self.peso1 == 0:
                                self.peso7 = 15
                        elif self.peso1 == 1:
                                self.peso7 = 16
                        self.dica7 = "-Sempre esconda os produtos de limpezas em locais que a criança não consiga acessar\n"
                elif opcao == "NÃO":
                        self.peso7 = 0
                        self.dica7 = ""
