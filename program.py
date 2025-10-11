# Librări

from random import randint
from machine import Pin, SPI, time_pulse_us
from utime import sleep
from ssd1309 import Display

# Variabile

latime_ecran=128
inaltime_ecran=64

x1=35
y1=6
text1="MoodBox"

x2=32
y2=50
rad1=10

x3=64
y3=50
rad2=10

x4=96
y4=50
rad3=10

btn1_pin=4
btn2_pin=5
btn3_pin=6

trig=Pin(3, Pin.OUT)
echo=Pin(2, Pin.IN)
senzor=True

hold=True

# Program

def dist():
    trig.low()
    sleep(0.2)
    trig.high()
    sleep(0.3)
    trig.low()
    
    # Măsurăm durata impulsului de la echo
    duration = time_pulse_us(echo, 1)
    
    # Calculăm distanța (viteză sunetului ~34300 cm/s)
    distance = (duration * 0.0343) / 2
    return distance

def main():
    
    # Comunicare cu ecranul, butoanele și senzor
    
    spi = SPI(1, baudrate=10_000_000, sck=Pin(10), mosi=Pin(11))
    display = Display(spi, dc=Pin(13), cs=Pin(9), rst=Pin(12))
    
    btn1 = Pin(btn1_pin, Pin.IN, Pin.PULL_UP)
    btn2 = Pin(btn2_pin, Pin.IN, Pin.PULL_UP)
    btn3 = Pin(btn3_pin, Pin.IN, Pin.PULL_UP)
    
    
    def elem():
        # Inițializare ecran
        
        display.contrast(0)
        display.draw_rectangle(0,0, latime_ecran, inaltime_ecran)
        
        # Elementele principale
        
        display.draw_text8x8(x1, y1, f"{text1}")
        display.draw_rectangle(x1-2, y1-2, (len(text1)*8)+4, y1+5)
        
        display.draw_text8x8(15, 16, "Cum te simti")
        display.draw_text8x8(47, 24, "azi?")
        
        # Stări/fețe
        
        display.draw_circle(x2, y2, rad1)
        display.fill_circle(x2-4, y2-2, rad1-8)
        display.fill_circle(x2+4, y2-2, rad1-8)
        display.draw_arc(x2, y2, 6, 30, 150)
        
        display.draw_circle(x3, y3, rad2)
        display.fill_circle(x3-4, y3-2, rad2-8)
        display.fill_circle(x3+4, y3-2, rad2-8)
        display.draw_line(x3-4, y3+4, x3+4, y3+4)
        
        display.draw_circle(x4, y4, rad3)
        display.fill_circle(x4-4, y4-2, rad3-8)
        display.fill_circle(x4+4, y4-2, rad3-8)
        display.draw_arc(x4, y4+9, 6, 210, 330)
        
        display.present()
        
    def sfat(text2="", text3="", text4="", text5=""):
        # Inițializare ecran
        
        display.contrast(0)
        display.draw_rectangle(0,0, latime_ecran, inaltime_ecran)
        
        # Elementele principale
        
        display.draw_text8x8(x1, y1, f"{text1}")
        display.draw_rectangle(x1-2, y1-2, (len(text1)*8)+4, y1+5)
        
        display.draw_text8x8(2, 16, f"{text2}")
        display.draw_text8x8(2, 24, f"{text3}")
        display.draw_text8x8(2, 32, f"{text4}")
        display.draw_text8x8(2, 40, f"{text5}")
        display.draw_text8x8(0, 48, "Apropie senzorul")
        display.draw_text8x8(19, 55, "pentru casa")
        display.present()
            
        
    elem()
    
    # Așteaptă semnal de la butoane
    
    global hold
    global senzor
    
    while hold:
        if btn1.value() == 0:
            
            # Șterge ce era pe ecran și alege un număr la întâmplare pentru a alege sfatul
            
            hold = False
            
            display.clear()
            
            nr = randint(1,4)
            
            if nr == 1:
                sfat("Zambeste! Lumea", "e mai buna cand", "tu zambesti.")
            elif nr == 2:
                sfat("Astazi e un nou", "inceput plin de", "oportunitati.")
            elif nr == 3:
                sfat("Fericirea ta", "face lumea mai", "luminoasa.")
            elif nr == 4:
                sfat("Raspandeste", "bucurie oriunde", "mergi.")
            
            # Dacă e ceva în fața senzorului la mai puțin de 5 cm, dute acasă (execută elem())
            
            while True:
                if dist() <= 5:
                    break
                sleep(0.2)
                
            display.clear()
            elem()
            hold = True
            
        elif btn2.value() == 0:
            
            # Șterge ce era pe ecran și alege un număr la întâmplare pentru a alege sfatul
            
            hold = False
            
            display.clear()
            
            nr = randint(1,4)
            
            if nr == 1:
                sfat("Ia o pauza,", "meriti sa", "respiri.")
            elif nr == 2:
                sfat("Odihna te face", "mai puternic.")
            elif nr == 3:
                sfat("Marile", "realizari incep", "cu un moment de", "liniste.")
            elif nr == 4:
                sfat("Relaxeaza-te...", "totul va fi", "bine.")
            
            # Dacă e ceva în fața senzorului la mai puțin de 5 cm, dute acasă (execută elem())
            
            while True:
                if dist() <= 5:
                    break
                sleep(0.2)
                
            display.clear()
            elem()
            hold = True
        
        elif btn3.value() == 0:
            
            # Șterge ce era pe ecran și alege un număr la întâmplare pentru a alege sfatul
            
            hold = False
            
            display.clear()
            
            nr = randint(1,4)
            
            if nr == 1:
                sfat("Respira adanc..", "totul e sub", "control.")
            elif nr == 2:
                sfat("Fiecare pas mic", "conteaza.")
            elif nr == 3:
                sfat("Nu trebuie sa", "faci totul", "perfect azi.")
            elif nr == 4:
                sfat("Esti mai", "puternic decat", "crezi.")
            
            # Dacă e ceva în fața senzorului la mai puțin de 5 cm, dute acasă (execută elem())
            
            while True:
                if dist() <= 5:
                    break
                sleep(0.2)
                
            display.clear()
            elem()
            hold = True

main()
