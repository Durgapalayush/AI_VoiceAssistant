from gtts import gTTS
import os

# Text to be converted to speech in Hindi
text_in_hindi = "यश अध्ययन करो अपना समय क्यों बर्बाद कर रहे हो।"

# Specify the language for Hindi
language = 'hi'  # Hindi

# Create a gTTS object with the specified text and language
tts = gTTS(text=text_in_hindi, lang=language, slow=False)

# Save the speech as an audio file
tts.save("output_hindi.mp3")

# Play the audio file (requires a program that can play MP3 files, e.g., VLC)
os.system("start output_hindi.mp3")