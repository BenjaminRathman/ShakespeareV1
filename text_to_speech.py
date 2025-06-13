import pyttsx3

class TextToSpeech:
    def __init__(self):
        # Initialize the TTS engine
        self.engine = pyttsx3.init()
        
        # Get available voices
        self.voices = self.engine.getProperty('voices')
        
        # Set default voice (usually the first one)
        self.engine.setProperty('voice', self.voices[0].id)
        
        # Set default rate (speed)
        self.engine.setProperty('rate', 150)  # Default is 200
        
    def list_voices(self):
        """List all available voices"""
        print("\nAvailable voices:")
        for i, voice in enumerate(self.voices):
            print(f"{i}: {voice.name}")
            
    def set_voice(self, voice_index):
        """Set the voice to use"""
        if 0 <= voice_index < len(self.voices):
            self.engine.setProperty('voice', self.voices[voice_index].id)
            print(f"Voice set to: {self.voices[voice_index].name}")
        else:
            print("Invalid voice index")
            
    def set_rate(self, rate):
        """Set the speaking rate (words per minute)"""
        self.engine.setProperty('rate', rate)
        print(f"Rate set to: {rate}")
        
    def speak(self, text):
        """Convert text to speech"""
        try:
            print("\nSpeaking...")
            self.engine.say(text)
            self.engine.runAndWait()
            print("Done speaking!")
        except Exception as e:
            print(f"Error during speech: {e}")

def main():
    tts = TextToSpeech()
    
    print("Welcome to Text-to-Speech!")
    print("Type 'quit' to exit")
    print("Type 'voices' to list available voices")
    print("Type 'voice X' to set voice (where X is the voice number)")
    print("Type 'rate X' to set speaking rate (where X is words per minute)")
    
    while True:
        print("\nEnter text to speak (or a command):")
        text = input("> ")
        
        if text.lower() == 'quit':
            break
        elif text.lower() == 'voices':
            tts.list_voices()
        elif text.lower().startswith('voice '):
            try:
                voice_index = int(text.split()[1])
                tts.set_voice(voice_index)
            except:
                print("Invalid voice number")
        elif text.lower().startswith('rate '):
            try:
                rate = int(text.split()[1])
                tts.set_rate(rate)
            except:
                print("Invalid rate number")
        else:
            tts.speak(text)
    
    print("Goodbye!")

if __name__ == "__main__":
    main() 