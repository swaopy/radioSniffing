# radio_send_images_caesar.py

from microbit import *
import radio

''' Function converts plaintext to ciphertext using key '''

def caesar(key, word):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in word:
        
        letter = letter.upper()
        index = ( alpha.find(letter) + key ) % 26
        result = result + alpha[index]
    
    return result

''' Script starts from here... '''

radio.on()
radio.config(channel=7)

sleep(1000)

string_list = ["HAPPY", "SAD", "ANGRY"]

while True:
    
    for packet in string_list:
        print("packet:", packet)
        display.show(getattr(Image, packet))
        packet = caesar(3, packet)
        print("Send encrypted:", packet)
        radio.send(packet)
        sleep(2500)