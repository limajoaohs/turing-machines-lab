import curses
import time

def caixa(stdscr):
    #limpa a tela
    stdscr.clear()

    #coordenadas da caixa
    altura, largura = 5, 60
    coord_y, coord_x = 12, 50

    #insere a janela das coordenadas
    window = curses.newwin(altura, largura, coord_y, coord_x)
    #cria um contorno
    window.box()

    #texto inicial
    texto_inicial = 'Encare seu destino, imaculado.'
    frase = ''

    #aparece uma letra por vez
    for letra in texto_inicial:
        frase += letra
        window.addstr(2, 14, frase)
        window.refresh()
        time.sleep(0.1)

    window.getch()
    
curses.wrapper(caixa)