# MEDIDOR DE ALTURA PARA ARPOVAÇÃO DE ENTRADA
from time import sleep # apenas adiciona tempo e interatividade ao programa
alturas = (1.73, 1.81, 1.85) #Variáveis que recebe a altura da pessoa


for c in alturas: # A variável "c" percorre a lista "alturas" e recebe seu valor a cada iteração
	print('\nBem vindo(a) ao Parque!!\n')
	sleep(3)
	print('Sua altura será medida para que possa entrar neste brinquedos.')
	sleep(3)
	if c >= 1.80: # Condicional que verifica altura mínima
		print('\nLENDO ALTURA...\n')
		sleep(3)
		print(f'Você possui {c}m de altura.\n'
			  f'Pode entrar!! Divirta-se!!')
		sleep(2)
	else: # Apresenta mensagem caso a condição IF acima for falsa
		print('\nLENDO ALTURA...\n')
		sleep(3)
		print(f'Sua altura está abaixo do mínimo permitido. '
			  f'\nVocê possui {c}m de altura.\nALTURA MÍNIMA 1.80m!!'
			  f'\nENTRADA NÃO PERMITIDA!!')
		sleep(2)


