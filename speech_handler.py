import speech_recognition as sr # type: ignore
import threading
import time

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio_data = None
        self.is_processing = False
        
    def listen_and_convert(self):
        """
        Listens to microphone input until Enter is pressed, then converts speech to text.
        Returns the converted text or None if there was an error.
        """
        try:
            with sr.Microphone() as source:
                print("Listening... Press Enter when you're done speaking!")
                # Adjust for ambient noise with longer duration
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Adjust sensitivity settings
                self.recognizer.energy_threshold = 400  # Increased threshold to reduce background noise
                self.recognizer.dynamic_energy_threshold = True
                self.recognizer.dynamic_energy_adjustment_damping = 0.15
                self.recognizer.dynamic_energy_ratio = 1.5
                self.recognizer.pause_threshold = 0.8  # Increased pause threshold to capture longer phrases
                
                # Start listening in a separate thread
                self.audio_data = None
                self.is_processing = True
                
                def listen_thread():
                    nonlocal source
                    try:
                        print("Speak now!")
                        self.audio_data = self.recognizer.listen(source, timeout=15, phrase_time_limit=15)
                        print("Finished recording audio")
                    except sr.WaitTimeoutError:
                        print("No speech detected within timeout period")
                    except Exception as e:
                        print(f"Error in listening thread: {e}")
                    finally:
                        self.is_processing = False
                
                # Start the listening thread
                thread = threading.Thread(target=listen_thread)
                thread.start()
                
                # Wait for Enter key
                input()
                print("Processing your speech...")
                
                # Wait for the listening thread to finish
                while self.is_processing:
                    time.sleep(0.1)
                
                thread.join(timeout=2)  # Give extra time for the thread to finish
                
                if self.audio_data:
                    print("Converting speech to text...")
                    text = self.recognizer.recognize_google(self.audio_data)
                    print(f"You said: {text}")
                    return text
                else:
                    print("No speech detected.")
                    return None
                
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from speech recognition service; {e}")
            return None

# Example usage
if __name__ == "__main__":
    speech_handler = SpeechHandler()
    text = speech_handler.listen_and_convert()
    if text:
        print("Text ready for processing:", text) 