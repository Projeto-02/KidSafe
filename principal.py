# As funções que serão utilizadas no código são majoritariamente puxadas do código que está escrito em Funções.py
from Funcoes import Formulario

# Import feito para pegar a data do dia certo, import esse que vai ser util no futuro para proibir a pessoa de fazer o formulario novamente dentro de 30 dias
from datetime import date

data = date.today()
data_atual = str(data.day) + "/" + str(data.month) + "/" + str(data.year)

funcoes = Formulario()

opcao = ""
dicas = ""
cont = 0

# Login
funcoes.login()

while opcao != "SAIR":
    # Tela de início
    print("Cadastrar criança\n")
    print("Crianças registradas\n")
    print("Testes passados\n")
    print("(Ou Sair para finalizar código)\n")
    print("\n")
    opcao = input("")
    opcao = opcao.upper()
    print("\n")

    # Cadastrar criança
    if opcao == "CADASTRAR CRIANÇA":
        funcoes.cadastrar_c()

    elif opcao == "CRIANÇAS REGISTRADAS":
        manipulador = open("Cadastros_crianças.txt", "r", encoding="utf8")
        for linha in manipulador:
            cada_linha = linha.strip()
            if len(cada_linha) != 0:
                print(cada_linha)
                print("\n")
            else:
                print("\nNenhuma criança registrada até o momento\n")
        manipulador.close()
        opcao = input("Escreva o nome de uma das crianças registradas:")
        opcao = opcao.upper()
        manipulador = open("Cadastros_crianças.txt", "r", encoding="utf8")
        for linha in manipulador:
            cada_linha = linha.strip()
            cada_linha = cada_linha.upper()
            if len(cada_linha) != 0:
                if opcao == cada_linha:
                    cont = 1
                    nome_do_filho = cada_linha
        manipulador.close()

        # O "cont" é utilizado para saber se a criança escolhida está cadastrada
        if cont == 1:
            # Pegunta 1
            funcoes.pergunta_1()

            # Pergunta 2
            funcoes.pergunta_2()

            # Pergunta 3
            funcoes.pergunta_3()

            # Como ira sair as dicas no final
            dica1 = funcoes.dica1
            dica2 = funcoes.dica2
            dica3 = funcoes.dica3
            dicas = dica1 + dica2 + dica3

            # valores que foram utilizados como peso foram calculados manualmente
            peso1 = funcoes.peso1
            peso2 = funcoes.peso2
            peso3 = funcoes.peso3
            # Média de segurança da criança
            seguranca = peso1 + peso2 + peso3

            # Escrever no txt
            manipulador = open('testes.txt', "a", encoding='utf8')
            manipulador.write("-----------")
            manipulador.write(data_atual)
            manipulador.write("-----------\n")
            manipulador.write("-------------")
            manipulador.write(nome_do_filho)
            manipulador.write("-------------\n")
            manipulador.write("-------Nível de segurança:-------\n")
            manipulador.write("--------------")
            manipulador.write(str(seguranca))
            manipulador.write(" %--------------\n")
            manipulador.write("-------------Dicas:-------------\n")
            manipulador.write(dicas)
            manipulador.write("\n\n")
            manipulador.close()
            print("\n")

    # Testes passados
    if opcao == "TESTES PASSADOS":
        manipulador = open('testes.txt', "r", encoding='utf8')
        texto = manipulador.read()
        if len(texto) != 0:
            print(texto)
        else:
            print("Nenhum teste realizado até o momento.\n")
        manipulador.close()
