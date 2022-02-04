from PySimpleGUI import PySimpleGUI as psgui

# Layout
psgui.theme('Reddit')
layout = [ 
    [psgui.Text('Digite seu nome: '),psgui.Input(key='nome', size=(30,1))],
    [psgui.Text('Digite seu stand: '),psgui.Input(key='stand', size=(30,1))],
    [psgui.Button('Concluir'), psgui.Button('Sair')]
]

# Janela
janela = psgui.Window('Python Bizarre Adventure', layout, enable_close_attempted_event=True)
while True:
    eventos, valores = janela.read()
    # Caso seja encerrado ou clicado no botão Sair
    if eventos in (psgui.WINDOW_CLOSE_ATTEMPTED_EVENT, 'Sair') and psgui.popup_yes_no('Deseja finalizar a aplicação?') == 'Yes':
        break
    # Caso seja clicado em Concluir
    if eventos == 'Concluir':
	# Caso os campos não forem vazios
        if valores['nome'] != '' and valores['stand'] != '':
            psgui.Popup('Nome: ' + valores['nome'], 'Stand: ' + valores['stand'])
            break
janela.close()