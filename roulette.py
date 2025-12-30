#!/usr/bin/python3
# A simple Russian Roulette Game

# Secrets es para mejor aleatorizacion ;)
import secrets
from pystyle import Colorate, Colors
# from colorama import Fore # Aun no la voy a usar, por el momento

# Funcion para mostrar el estado actual de cada ronda
def estado_actual(bot, user, bullets, bedrooms):
    print(Colorate.Horizontal(Colors.rainbow, f"Vidas\nBOT : [{bot}]\nUSER : [{user}]"))

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
    bot = 5
    user = 5
    bullets = 1
    bedrooms = 6

    for ronda_actual in range(1, r + 1):
        estado_actual(bot, user, bullets, bedrooms)



# Nota, aun no termino el codigo, esperen actualizaciones
rounds(r=6)