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
        self.engine.setProperty('rate', 220)  # Default is 200
        
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
            
            self.engine.say(text)
            self.engine.runAndWait()
            
        except Exception as e:
            print(f"Error during speech: {e}")

# Example usage (only runs when file is executed directly)
if __name__ == "__main__":
    tts = TextToSpeech()
    tts.speak("Enter text to speak:")

