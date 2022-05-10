# radio_send_images.py

from microbit import *
import radio

radio.on()
radio.config(channel=7)

sleep(1000)
string_list = ["HAPPY", "SAD", "ANGRY"]
while True:
    
    
    for packet in string_list:
        print("Send:", packet)
        radio.send(packet)
        sleep(2500)