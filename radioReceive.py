# radio_receive_images.py

from microbit import *
import radio

radio.on()
radio.config(channel=7)

sleep(1000)

while True:
    
    packet = radio.receive()

    if packet:
        print("Receive:", packet)
        display.show(getattr(Image, packet))