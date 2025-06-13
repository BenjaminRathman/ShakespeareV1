import os
from dotenv import load_dotenv
import anthropic

class ClaudeAPI:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variable
        self.api_key = os.getenv('CLAUDE_API_KEY')
        if not self.api_key:
            raise ValueError("CLAUDE_API_KEY not found in environment variables")
            
        # Initialize the Anthropic client
        self.client = anthropic.Anthropic(api_key=self.api_key)
        
    def get_response(self, prompt, model="claude-3-opus-20240229"):
        """
        Get a response from Claude
        
        Args:
            prompt (str): The prompt to send to Claude
            model (str): The model to use (default is claude-3-opus-20240229)
            
        Returns:
            str: Claude's response
        """
        try:
            message = self.client.messages.create(
                model=model,
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Error getting response from Claude: {e}")
            return None

# Example usage
if __name__ == "__main__":
    try:
        claude = ClaudeAPI()
        response = claude.get_response("Hello, how are you?")
        if response:
            print("Claude's response:", response)
    except Exception as e:
        print(f"Error: {e}") 