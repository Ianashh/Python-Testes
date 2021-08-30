class Carros:
    def __init__(self):
        self.marca = [input("Digite a marca do veículo:\t").upper()]
        self.modelo = [input("\nDigite o modelo do veículo:\t").upper()]
        self.ano = [int(input("\nDigite o ano do veículo:\t"))]
        self.placa_letra = [input("\nDigite as letras da placa do veículo:\t").upper()]
        self.placa_num = [int(input("\nDigite os números da placa do veículo:\t"))]

c1 = Carros()
print(f"\nMARCA:\t{c1.marca}\nMODELO:\t{c1.modelo}\nANO:\t{c1.ano}\nPLACA:\t{c1.placa_letra}-{c1.placa_num}\n\n")
#for c in Carros:
#    print(f"\nMARCA:\t{c.marca}\nMODELO:\t{c.modelo}\nANO:\t{c.ano}\nPLACA:\t{c.placa_letra}-{c.placa_num}\n\n")
