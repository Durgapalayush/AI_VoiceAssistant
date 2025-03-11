import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech

# Set the voice (you might need to adjust the voice index based on available voices)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Select a male voice

# Text to be converted to speech
text = "This is a sample text in a male Indian accent."

# Convert the text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
