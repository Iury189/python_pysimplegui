from PySimpleGUI import PySimpleGUI as psgui
import time

# Layout
psgui.theme('Reddit')
layout = [ 
    [psgui.Text('Digite seu nome: '),psgui.Input(key='nome', size=(25,1))],
    [psgui.Text('Digite seu stand: '),psgui.Input(key='stand', size=(25,1))],
    [psgui.Button('Concluir'), psgui.Button('Sair')]
]

# Janela
janela = psgui.Window('Python Bizarre Adventure', layout)
while True:
    eventos, valores = janela.read()
    # Caso seja encerrado ou clicado no botão Sair
    if eventos in (psgui.WINDOW_CLOSED, 'Sair'):
        break
    # Caso seja clicado em Concluir
    if eventos == 'Concluir':
	# Caso os campos não forem vazios
        if valores['nome'] != '' and valores['stand'] != '':
            print ('Golden Wing!')
            time.sleep(3)
            break
janela.close()