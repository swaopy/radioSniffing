# countdown_receiver_encrypted.py

from microbit import *
import radio

# Step 1: Add the cipher function below the transmitter
# script’s import statements. (6 statements)

def ascii_shift(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result

# Step 2: Set a key to decrypt with a statement like key = -5.

key = -5

radio.on()
radio.config(channel=7,length=50)

sleep(1000)

print("Countdown App")
print("micro:bit receiver\n")

while True:
    packet = radio.receive()
    if packet is not None:
        print("Receive encrypted: ", packet)  # <- add
        
        # Step 3: Call the cipher function to decrypt the data
        # after receiving/before using the packet.

        packet = ascii_shift(key, packet)
        
        print("packet: ", packet)             # <- change
        
        print("Receive: ", packet)

        print()
        print("Parse: ")

        dictionary = eval(packet)

        value = dictionary['start']
        message = dictionary['after']
        
        print("value = ", value)
        print("message = ", message, "\n")
        
        while value >= 0:
            print(value)
            sleep(1000)
            value = value - 1
            
        print(message)
        
        print()