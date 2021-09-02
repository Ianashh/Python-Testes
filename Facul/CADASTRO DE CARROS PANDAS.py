# -----------------------------------------------------------------------------------------------------------------------
# Passo 1 - Estabelecer variáveis e importar libs
from time import sleep
import pandas as pd
carros = {'MARCA': ["", "", "", "", "", "", "", "", "", ""],
          'MODELO': ["", "", "", "", "", "", "", "", "", ""],
          'ANO': [0,0,0,0,0,0,0,0,0,0],
          'L_PLACA': ["", "", "", "", "", "", "", "", "", ""],
          'N_PLACA': ["", "", "", "", "", "", "", "", "", ""]}
opcao = 0
#-----------------------------------------------------------------------------------------------------------------------
# Passo 2 - Estabelece o Menu
print("\n\033[1;32m")
print("=-" * 27)
print("\t\t\t\t\tOlá usuário!!"
      "\n   Esse é o sistema de cadastramento de veículos !!")
print("=-" * 27, "\n\033[m")
sleep(2)

while opcao != 9:
    opcao = int(input('\t\t\t\033[1;4;31mMENU\n''\033[m'
                      '\033[1;33m''[1]''\033[m''\033[1;34m''INSERIR NOVO VEÍCULO''\033[m''\n'
                      '\033[1;33m''[2]''\033[m''\033[1;34m''LISTAR VEÍCULOS CADASTRADOS''\033[m''\n'
                      '\033[1;33m''[3]''\033[m''\033[1;34m''PESQUISAR POR ANO DE FABRICAÇÃO''\033[m''\n'
                      '\033[1;33m''[4]''\033[m''\033[1;34m''LISTAR EM ORDEM DECRESCENTE DO ANO DE FABRICAÇÃO'
                      '\033[m''\n''\033[1;33m''[5]''\033[m''\033[1;34m''LISTAR POR MODELO''\033[m''\n'
                      '\033[1;33m''[9]''\033[m''\033[1;34m''SAIR DO PROGRAMA''\033[m''\n'
                      '\033[1;4;33m\nDIGITE UMA OPÇÃO:\033[m '))
    print("\n")
#-----------------------------------------------------------------------------------------------------------------------
# Passo 3 - Cadastro dos carros:
    if opcao == 1:
        escolha = int(input("\033[1;33mQuantos carros deseja cadastrar: \033[m"))
        if escolha > 10:
            print("\033[1;31mNão é possível inserir mais que 10 veículos por vez!!\n")

        else:
            for n in range(0, escolha):
                print('\n')
                print("=-" * 27)
                print(f"\t\t\t   CADASTRE O VEÍCULO 0{n + 1} !!")
                print("=-" * 27, "\n")

                carros["MARCA"][n] = input("\033[1mDigite a marca do veículo: ").upper().strip()
                carros["MODELO"][n] = input("Digite o modelo do veículo: ").upper().strip()
                carros["ANO"][n] = int(input("Digite o ano de fabricação do veículo: "))
                carros["L_PLACA"][n] = input("Digite as 3 letras da placa do veículo: ").upper().strip()
                carros["N_PLACA"][n] = input("Digite os 4 números da placa do veículo: \033[m")
                print("\n\033[1;32m")
                print("=-" * 27)
                print(f"\t\t VEÍCULO 0{n + 1} CADASTRADO COM SUCESSO!!")
                print("=-" * 27, "\n\033[m")
                df_carros = pd.DataFrame(carros)

#-----------------------------------------------------------------------------------------------------------------------
# Passos 4 - Listar veículos:
    elif opcao == 2:
        r_ordem = df_carros.sort_values(by=['ANO'], ascending=False)
        print(r_ordem)


#-----------------------------------------------------------------------------------------------------------------------
# Passos 5 - Listar veículos por ano:
    elif opcao == 3:
        pesquisa = int(input("\n\n\033[1mQual ano deseja pesquisar: \033[m"))
        pesq_ano = df_carros[df_carros['ANO'] == pesquisa]
        print(pesq_ano)
        print('\n')

#-----------------------------------------------------------------------------------------------------------------------
# Passos 6 - Listar veículos por ordem  ano:
    elif opcao == 4:
        descendente = int(input("\n\n\033[1mDigite o ano para verificar os "
                                "veículos cadastrados de forma decrescente: \033[m"))
        pesq_desc = r_ordem[r_ordem['ANO'] <= descendente]
        print(pesq_desc)

#-----------------------------------------------------------------------------------------------------------------------
# Passos 7 - Listar veículos por modelo:
    elif opcao == 5:
        modelo = input("\n\n\033[1mDigite modelo do veículo para buscar: \033[m").upper().strip()
        pesq_modelo = r_ordem[r_ordem['MODELO'] == modelo]
        print(pesq_modelo)

#-----------------------------------------------------------------------------------------------------------------------
# Passos 8 - Finalizar programa:
    elif opcao == 9:
      print('\033[31m' f'\nO programa está se encerrando!!')
      sleep(1)
      print('....5')
      sleep(1)
      print('...4')
      sleep(1)
      print('..3')
      sleep(1)
      print('.2')
      sleep(1)
      print('1')
      sleep(2)
      print('PROGRAMA FINALIZADO! ATÉ BREVE!!''\033[m')
      break

    else:
        print(f'\033[1;31m{opcao} não é um número de uma opção válida no menu!! \n\nDigite outra opção!!\033[m\n\n')