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

# Step 2: Set an encryption key with a statement like key = 5.

key = 5

radio.on()
radio.config(channel=7,length=50)

sleep(1000)

print("Countdown App")
print("micro:bit sender")

while True:
    text = input("Enter countdown start: ")
    value = int(text)
    message = input("Enter message after countdown: ")
    
    dictionary = {  }
    dictionary['start'] = value
    dictionary['after'] = message

    packet = str(dictionary)
    
    print("Send: ", packet)

    # Step 3: Call the cipher function to encrypt the data
    # before sending the packet.

    packet = ascii_shift(key, packet)

    radio.send(packet)
    
    print()