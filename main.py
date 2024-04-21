import os
import requests
from playsound import playsound



# URL of the mp3 file
url = "http://192.168.90.251:5000/speech"

# Send GET request
response = requests.get(url)

# Save the mp3 file
with open('speech.mp3', 'wb') as file:
    file.write(response.content)

# Play the mp3 file
if os.path.isfile('speech.mp3'):
        # Play the mp3 file
        print("Playing the mp3 file...")
        playsound('speech.mp3')
else:
        print("The file does not exist or is not valid.")

