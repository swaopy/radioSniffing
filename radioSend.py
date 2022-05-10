# radio_send_images.py

from microbit import *
import radio

radio.on()
radio.config(channel=7)

sleep(1000)

while True:
    
    packet = "HAPPY"
    print("Send:", packet)
    radio.send(packet)
    sleep(2500)
    
    packet = "SAD"
    print("Send:", packet)
    radio.send(packet)
    sleep(2500)

    packet = "ANGRY"
    print("Send:", packet)
    radio.send(packet)
    sleep(2500)