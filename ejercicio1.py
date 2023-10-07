from gpiozero import LED, Button
from signal import pause

verde = LED(17)
ambar = LED(27)
rojo = LED(22)
boton = Button(2)

def siguiente_led():
    if verde.is_lit:
        verde.off()
        ambar.on()
    elif ambar.is_lit:
        ambar.off()
        rojo.on()
    else:
        rojo.off()
        verde.on()

boton.when_pressed = siguiente_led

verde.on()
pause()