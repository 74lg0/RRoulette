#!/usr/bin/python3
# A simple Russian Roulette Game

# Secrets es para mejor aleatorizacion ;)
import secrets
from pystyle import Colorate, Colors
import time
import os
# from colorama import Fore # Aun no la voy a usar, por el momento

def clear():
    os.system('cls' if os.name == "nt" else 'clear')

# Animación para la carga de balas
def char_bull(b, bedrooms):
    recamara = "┃"
    bala = "█"

    for b in range(b):
        print(Colorate.Horizontal(Colors.rainbow, bala), end='')

    for r in range(bedrooms - b):
        print(Colorate.Horizontal(Colors.rainbow, recamara), end='')
    
    time.sleep(0.1)


# Funcion para mostrar el estado actual de cada ronda
def estado_actual(bot, user, bullets, bedrooms):
    banner = f'''
========== Vidas ==========
BOT     : {bot}
USER    : {user}
===========================
BALAS   : '''

    # Animacion
    for b in range(bedrooms):
        clear()
        print(Colorate.Horizontal(Colors.rainbow, banner), end='')
        char_bull(bullets, b)

# Funcion para calcular la probabilidad de morir
def c_death(bullets, bedrooms):
    # Probabilidad de morir P = (Balas / Recámaras) * 100
    p = (bullets / bedrooms) * 100
    
    # Devolvemos la probabilidad en escala porcentual (100% MAX)
    return p


# Funcion para ¡Disparar!
def shot(bullets, bedrooms):
    # P(n < b)
    # P(n=1 < b=6)
    # Si n (Sea este el numero de balas) es menor que b (Sea este la cantidad de recámaras)
    # ¡Dispara!
    # PD: Con cada disparo se gira el tambor
    g = secrets.randbelow(bedrooms)+1
    return g <= bullets # True (Muerte), False (Vida)

# Configuramos al bot
def ai_bot(bullets, bedrooms):
    p = c_death(bullets, bedrooms)
    return p <= 35 # True si es menor o igual a 35, de lo contrario False


# Funcion para las rondas
def rounds(r):
    # Variables iniciales
    bot = 5 # Vidas iniciales = 5
    user = 5
    bullets = 1 # Balas = (r) Por cada ronda se suma +1 bala
    bedrooms = 6 #Cámaras, aquí son 6

    for ronda_actual in range(1, r + 1):
        estado_actual(bot, user, bullets, bedrooms)



# Nota, aun no termino el codigo, esperen actualizaciones
rounds(r=6)