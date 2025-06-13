from UserInteractionHandlers.speech_handler import SpeechHandler
from StoryTellerEngine.api_connections import ClaudeAPI
from UserInteractionHandlers.text_to_speech import TextToSpeech

class VoiceAssistant:
    def __init__(self):
        # Initialize all components
        self.speech_handler = SpeechHandler()
        self.claude = ClaudeAPI()
        self.tts = TextToSpeech()
        
        # Set a default system instruction for Claude
        self.system_instruction = "You are a helpful AI assistant. Provide clear and concise responses."
        
    def run(self):
        """Run the voice assistant"""
        print("Voice Assistant Ready!")
        print("Press Enter to start speaking, then press Enter again when done.")
        print("Type 'quit' to exit")
        
        while True:
            input("\nPress Enter to speak...")
            
            # Listen for voice input
            print("Listening... Press Enter when done!")
            text = self.speech_handler.listen_and_convert()
            
            if text:
                print(f"You said: {text}")
                
                # Get response from Claude
                print("Getting response from Claude...")
                full_prompt = f"{self.system_instruction}\n\nUser: {text}"
                response = self.claude.get_response(full_prompt)
                
                if response:
                    print(f"Claude's response: {response}")
                    
                    # Speak the response
                    print("Speaking response...")
                    self.tts.speak(response)
                else:
                    print("Sorry, I couldn't get a response from Claude.")
            else:
                print("No speech detected.")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run() 