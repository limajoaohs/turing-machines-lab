from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
from random import uniform
from time import sleep
import pyautogui as auto
import threading
import pygame


pygame.mixer.init()





prevent = 0  # Número inicial de cliques para ignorar
paused = True  # Flag para pausar ou continuar o programa

print('Macro iniciado')

def executar_acao():
    global paused, prevent
    if not paused:
        sleep(uniform(0.15, 0.5))
        auto.click()

def plim():
    global paused
    paused = not paused

def on_click(x, y, button, pressed):
    global prevent, paused

    if pressed:


        if button.name == 'left' and not paused:
            if prevent > 0:
                prevent -= 1  # Decrementa prevent a cada clique

            else:
                prevent = 4  # Reinicia o contador após a execução
                for i in range(prevent):
                    threading.Thread(target=executar_acao).start()



open_inv = False
def on_press(key): # Pausas e ativaçõesy
    global paused, open_inv
    try:
        if key.char == 'f':
            plim()

        elif key.char == 'e':
            if not paused and not open_inv:
                open_inv = True
                plim()

    except: pass

# Inicia os listenersz
def start_listeners():
    # Listener do mouse
    mouse_listener = MouseListener(on_click=on_click)
    mouse_listener.start()

    # Listener do teclado
    keyboard_listener = KeyboardListener(on_press=on_press)
    keyboard_listener.start()

    mouse_listener.join()
    keyboard_listener.join()

start_listeners()