# terminal_chat_through_microbits_encrypted_A.py
# learn.parallax.com/cyberbot
# Copyright Parallax Inc 2020 under MIT license

from microbit import *
import radio

''' Function converts plaintext to ciphertext using key '''
 
def ascii_shift(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result

 
''' Script starts from here... '''

radio.on()
radio.config(channel=7)

sleep(1000)

print("micro:bit transceiver A")
print()

text = input("Enter key: ")
key = int(text)

print()
print("Type messages, press enter to send.")
print("Received messages will also be displayed.")
print()

while True:
    if uart.any():
        tx = input("Send: ")
        tx = ascii_shift(key, tx)
        radio.send(tx)
    message = radio.receive()
    if message:
        message = ascii_shift(-key, message)
        print("Receive: ", message)