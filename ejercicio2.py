from gpiozero import LED
from time import sleep

verde = LED(17)
ambar = LED(27)
rojo = LED(22)

def semaforo():
    while True:
        eleccion = input("Ingrese una opción (verde, ambar, rojo): ").lower()
        if eleccion == 'verde':
            verde.on()
            ambar.off()
            rojo.off()
        elif eleccion == 'ambar':
            verde.off()
            ambar.on()
            rojo.off()
        elif eleccion == 'rojo':
            verde.off()
            ambar.off()
            rojo.on()
        else:
            print("Opción no válida. Intenta nuevamente.")

semaforo()