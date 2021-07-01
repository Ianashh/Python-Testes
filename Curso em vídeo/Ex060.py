# Obs.: usar # nas linhas do "for" (Passo 2.1) ou nas linhas do "while" (Passo 2.2) para anular um ou outro programa e obter o resultado correto.
# Passo 1: Criar variáveis
n = int(input('Digite um número para descobrir seu fatorial: '))
cont = n
esc = n

# Passo 2.1: Usar o "for" para o fatorial

for n in range(n,1,-1) :
        cont = cont*(n-1)

# Passo 3: Print do resultado

print(f'O número escolhido foi o {esc} e seu valor fatorial é {cont}')

# Passo 2.2: Usar o "while" para o fatorial

while esc != 1:
        esc -= 1
        cont = cont * esc

# Passo 3: Print do resultado

print(f'O número escolhido foi o {n} e seu valor fatorial é {cont}')
