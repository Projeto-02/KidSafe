# As funções que serão utilizadas no código são majoritariamente puxadas do código que está escrito em Funções.py
from Funcoes import Formulario

# Import feito para pegar a data do dia certo, import esse que vai ser util no futuro para proibir a pessoa de fazer o formulario novamente dentro de 15 dias
from datetime import date

from time import sleep

import os

#Função pega da internet para a pessoa apenas pressionar uma tecla para retornar
def _find_getch():
    try:
        import termios
    except ImportError:
        import msvcrt
        return msvcrt.getch

    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

getch = _find_getch()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def anykey():
    print('Pressione qualquer tecla para retornar')
    getch()

seconds = 2

data = date.today()
data_atual = str(data.day) + "/" + str(data.month) + "/" + str(data.year)
funcoes = Formulario()

dicas = ""
cont = 0
opcao = 5
i = 0
cont2 = 1
ver = 1
contador = 1
verificador = 0
criancas = []
nome_do_filho = ""

# Login
funcoes.login()

senha = funcoes.senha
email = funcoes.email
email_n = email + "\n"

manipulador = open("Cadastro.txt", "r", encoding = "utf8")
for linha in manipulador:
  if linha == email + "\n":
    i = 1
  elif i == 1:
    if linha == senha + "\n":
      opcao = 0
    i = 2
manipulador.close()

opc = funcoes.opc

if opc == 2:
  opcao = 0

if opcao == 5:
  print("\nCadastro não encontrado no sistema\n")

print("Espere 2 segundos\n")
sleep(seconds)
cls()


while opcao != 5:
    # Tela de início
    print("1 - Cadastrar criança\n")
    print("2 - Crianças registradas\n")
    print("3 - Testes passados\n")
    print("4 - Informações\n")
    print("5 - Sair\n")
    print("\n")
    opcao = int(input("Escolha uma da opções acima: "))
    print("\n")
    print("Espere 2 segundos")
    sleep(seconds)
    cls()
    cont2 = 1
    nome_do_filho = ""

    # Cadastrar criança
    if opcao == 1:
        funcoes.cadastrar_c()
        print("Espere 2 segundos")
        sleep(seconds)
        cls() 

    elif opcao == 2:
        print("crianças:\n\n")
        manipulador = open("Cadastros_crianças.txt", "r", encoding="utf8")
        for linha in manipulador:
            if linha == email_n:
                    verificador = 1
            elif verificador == 1:
                    print(cont2, " - ", linha)
                    verificador = 0
                    cont2 = cont2 + 1
                    criancas.append(linha)

        if cont2 == 1:
                print("Nenhuma criança registrada até o momento\n")
        else: 
                print("\n")
        manipulador.close()
        opcao = int(input("Escolha uma das crianças:"))
        if (opcao > 0) and (opcao <= cont2):
          nome_do_filho = criancas[opcao - 1]
        if nome_do_filho == "":
          print("\nCriança não está o sistema")
        print("Espere 1 segundos\n")
        sleep(seconds - 1)
        cls()

        # O "cont" é utilizado para saber se a criança escolhida está cadastrada
        if nome_do_filho != "":
            # Pegunta 1
            funcoes.pergunta_1()
            print("Espere 1 segundos\n")
            sleep(seconds - 1)
            cls()

            # Pergunta 2
            funcoes.pergunta_2()
            print("Espere 1 segundos\n")
            sleep(seconds - 1)
            cls()

            # Pergunta 3
            funcoes.pergunta_3()
            print("Espere 1 segundos\n")
            sleep(seconds - 1)
            cls()

            # Pergunta 4
            funcoes.pergunta_4()
            print("Espere 1 segundos\n")
            sleep(seconds - 1)
            cls()

            # Pergunta 5
            funcoes.pergunta_5()
            print("Espere 1 segundos\n")
            sleep(seconds - 1)
            cls()

            # Pergunta 6
            funcoes.pergunta_6()
            print("Espere 1 segundos\n")
            sleep(seconds - 1)
            cls()

            # Pergunta 7
            funcoes.pergunta_7()

            # Como ira sair as dicas no final
            dica2 = funcoes.dica2
            dica3 = funcoes.dica3
            dica4 = funcoes.dica4
            dica5 = funcoes.dica5
            dica6 = funcoes.dica6
            dica7 = funcoes.dica7
            dicas = dica2 + dica3 + dica4 + dica5 + dica6 + dica7

            # valores que foram utilizados como peso foram calculados manualmente
            peso2 = funcoes.peso2
            peso3 = funcoes.peso3
            peso4 = funcoes.peso4
            peso5 = funcoes.peso5
            peso6 = funcoes.peso6
            peso7 = funcoes.peso7
            # Média de segurança da criança
            seguranca = 100 - (peso2 + peso3 + peso4 + peso5 + peso6 + peso7)

            # Escrever no txt
            manipulador = open('testes.txt', "a", encoding='utf8')
            manipulador.write(email_n)
            manipulador.write("-----------")
            manipulador.write(data_atual)
            manipulador.write("-----------\n")
            manipulador.write("-------------")
            manipulador.write(nome_do_filho[0:-1])
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
            print("Espere 2 segundos\n")
            verificador = 0
            sleep(seconds)
            cls()

    # Testes passados
    elif opcao == 3:
        manipulador = open('testes.txt', "r", encoding='utf8')
        texto = manipulador.read()
        manipulador.close()
        manipulador = open('testes.txt', "r", encoding='utf8')
        if len(texto) == 0:
            print("Nenhum teste realizado até o momento.\n")
        else:
                for linha in manipulador:
                        if linha == "\n":
                                verificador = 0
                        elif verificador == 1:
                                print(linha)
                        elif linha == email_n:
                                verificador = 1
                                print("\n")
        manipulador.close()
        print("\n")
        anykey()
        print("Espere 2 segundos\n")
        sleep(seconds)
        cls()

    elif opcao == 4:
        contador = 1
        ver = 1
        manipulador = open("noticias.txt", "r", encoding="utf8")
        for linha in manipulador:
                cada_linha = linha.strip()
                if len(cada_linha) != 0:
                        if ver == contador:
                                print(contador, " - ", linha)
                                ver = ver + 1
                        else:
                                print(linha)
                else:
                        contador = contador + 1
        manipulador.close()
        print("\n")
        anykey()
        print("Espere 2 segundos\n")
        sleep(seconds)
        cls()

    elif (opcao > 5) or (opcao < 1):
      print("Digite um número válido\n\n")
      print("Espere 1 segundos\n")
      sleep(seconds - 1)
      cls()

if opcao == 5:
  print("Finalizando...")
  sleep(seconds)

