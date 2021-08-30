#-----------------------------------------------------------------------------------------------------------------------
# Passo 1 - Estabelecer variáveis e classes
from time import sleep

class Carros:
    def __init__(self,marca,modelo,ano,placa_letra,placa_num):
        self.marca= [input("Digite a marca do veículo: ").upper()]
        self.modelo = [input("\nDigite o modelo do veículo: ").upper()]
        self.ano = [int(input("\nDigite o ano do veículo: "))]
        self.placa_letra = [input("\nDigite as letras da placa do veículo: ").upper()]
        self.placa_num = [int(input("\nDigite os números da placa do veículo: "))]
carro = []
escolha, n = 0,0
num_carros = 0
carros_ordenados = []

#-----------------------------------------------------------------------------------------------------------------------
# Passo 2 - Estabelecer Menu

print("\n\033[1;32m","=-"*27)
print("\t\t\t\tOlá usuário!!"
      "\nEsse é o sistema de cadastramento de veículos !!")
print("=-"*27,"\n\033[m")
sleep(2)

while escolha != 9:
      escolha = int(input('\t\t\t\033[1;4;31mMENU\n''\033[m'
                          '\033[1;33m''[1]''\033[m''\033[1;34m''INSERIR NOVO VEÍCULO''\033[m''\n'
                          '\033[1;33m''[2]''\033[m''\033[1;34m''LISTAR VEÍCULOS CADASTRADOS''\033[m''\n'
                          '\033[1;33m''[3]''\033[m''\033[1;34m''LISTAR POR ANO DE FABRICAÇÃO''\033[m''\n'
                          '\033[1;33m''[4]''\033[m''\033[1;34m''LISTAR À PARTIR DE ALGUM ANO DE FABRICAÇÃO''\033[m''\n'
                          '\033[1;33m''[5]''\033[m''\033[1;34m''LISTRA POR MODELO''\033[m''\n'
                          '\033[1;33m''[9]''\033[m''\033[1;34m''SAIR DO PROGRAMA''\033[m''\n'
                          '\033[1;4;33m\nDIGITE UMA OPÇÃO:\033[m '))
      print("\n")
#-----------------------------------------------------------------------------------------------------------------------
# Passo 2 - Cadastro dos carros:

      if escolha == 1:

        num_carros = int(input("Quantos carros deseja inserir: "))
        if num_carros > 10:
            print("Não é possível inserir mais que 10 veículos por vez!!\n")

        else:
            for n in range(0, num_carros):
                carro.append(n)
                carro[n] = Carros(marca=[], modelo = [], ano = [], placa_letra = [], placa_num = [])

                print(f"\nMARCA:\t{carro[n].marca}\nMODELO:\t{carro[n].modelo}\nANO:\t{carro[n].ano}"
                      f"\nPLACA:\t{carro[n].placa_letra}-{carro[n].placa_num}\n\n")

            print("\n")
            print("=-"*27)
            print("\t\t   CARRO CADASTRADO COM SUCESSO!!")
            print("=-"*27,"\n")
        print(f"{carro[1].ano}{carro[0].ano}")
#        for c in range(0,len(carro)):
#            print(f"\nMARCA:\t{carro[c].marca}\nMODELO:\t{carro[c].modelo}\nANO:\t{carro[c].ano}"
#                              f"\nPLACA:\t{carro[c].placa_letra}-{carro[c].placa_num}\n\n")
#-----------------------------------------------------------------------------------------------------------------------
# Passos 3 - Listar veículos:

#      elif escolha == 2:
#        ordem = len(marca)
#        c = 0
#        while c < ordem:
#          print(f"\nMARCA:\t{marca[c]}\nMODELO:\t{modelo[c]}\nANO:\t{ano[c]}\nPLACA:\t{placa_let[c]}-{placa_num[c]}\n\n")
#          c += 1

#-----------------------------------------------------------------------------------------------------------------------
# Passo 4 - Listar por ano de fabricação:
      #elif escolha == 3:



#        """ordem = len(marca)
#        c = 0
#        while c < ordem:
#          print(f"\nMARCA:\t{marca[c]}\nMODELO:\t{modelo[c]}\nANO:\t{ano[c]}\nPLACA:\t{placa_let[c]}-{placa_num[c]}\n\n")
#          c += 1"""







      elif escolha == 9: # Funcionando finalizador do programa
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


print(f"{carro[1].ano}{carro[0].ano}")
#""" 2 - O sistema deverá oferecer, ao usuário, as seguintes funcionalidades:

#- Listar os veículos cadastrados;
#- Inserir um novo veículo;
#- Listar os veículos filtrando-se por ano de fabricação;
#- Listar os veículos com o ano de fabricação acima de um certo valor especificado pelo usuário
#- Listar os veículos filtrando-se pelo modelo.

# - O sistema deverá armazenar os veículos ordenados pelo ano de
#fabricação, ou seja, ao inserir um novo veículo, este deve ser
#inserido em ordem crescente de ano de fabricação."""

#""""""
