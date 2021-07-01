import pyautogui as pg
import pyperclip as pp

pg.alert('Certifique-se de ter minimizado o Firefox e deixado o e-mail .imob na segunda aba fixada!!\n ENJOY!!')

from time import sleep
mes = input('Qual nome do mês esse e-mail será enviado? ').strip().title()
assunto = (f"Olá Marinês, bom dia!! \n\nSegue anexo recibo para assinatura referente ao aluguel de {mes}.")
caminho = r'C:\Users\emers\OneDrive\Área de Trabalho\Trabalho\Locação\Maria Inês 1506\Evolution Home - Alto da Palhano - Ap 1506\Recibos Marinês'
pg.PAUSE = 2 #pausa a cada comando do pyautogui

pg.click(1788,10) # minimiza o pycharm
pg.click(88,1052) # seleciona o firefox (que esta minimizado) na primeira posição pós botão do Windows na barra de tarefas
pg.click(78,15) # clica na 2ª aba fixa do firefox já aberto
pg.click(139,250) # Seleciona novo e-mail no gmail
pg.write('maritomael') # Nome do destinatário do e-mail
pg.press('enter') # Seleciona destinatário
pg.press('tab') # pula para a barra assunto
pg.write('Recibo aluguel de ') # escreve parte do assunto
pp.copy(mes) # copia o mês digitado no inicio do programa
pg.hotkey('ctrl', 'v') # cola o mês ao final do assunto
pg.write(' !!!') # finaliza a mensagem do assunto
pg.press('tab') # pula para o corpo do texto
pp.copy(assunto) # copia a variável assunto
pg.hotkey('ctrl', 'v') # cola a variável assunto no corpo do e-mail
pg.click(x=1339, y=979) # seleciona anexar
pg.press('f4') # seleciona barra de endereço do windows explorer
pg.hotkey('ctrl','a') # seleciona todo o caminho escrito
pg.press('backspace') # apaga o caminho selecionado
pp.copy(caminho) # copia o caminho aqui disposto na variável
pg.hotkey('ctrl', 'v') # cola o caminho na barra de endereço
pg.press('enter') # seleciona a pasta destino
pg.click(x=580, y=141) # seleciona data de modifi
    # cação de arquivos
pg.click(x=425, y=186) # seleciona o primento arquivo
pg.click(x=350, y=152) # volta a configuração de organização por nome
pg.alert("VERIFIQUE SE FOI SELECIONADO O ARQUIVO CORRETO")  #pede para verificar o arquivo selecionado
pg.press('enter') # Inclui o arquivo selecionado ao e-mail
pg.alert('CLIQUE NA SETA AO LADO DE SEND APENAS UMA VEZ')  # pede para clicar no agendamento de envio para que não haja envio acidental do e-mails
sleep(5) #da um tempo de 5 segundos para execução do comando após o ok
pg.click(x=1263, y=948) # seleciona
pg.click(x=891, y=705)
pg.alert('PROGRAMA FINALIZADO')





#C:\Users\emers\OneDrive\Área de Trabalho\Trabalho\Locação\Maria Inês 1506\Evolution Home - Alto da Palhano - Ap 1506\Recibos Marinês