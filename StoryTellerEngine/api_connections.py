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
        
    def get_response(self, system_instruction, story_context, user_input, model="claude-3-opus-20240229"):
        try:
            message = self.client.messages.create(
                model=model,
                max_tokens=1000,
                system=system_instruction,
                messages=[
                    {"role": "user", "content": f"Story so far:\n{story_context}"},
                    {"role": "user", "content": user_input}
                ]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Error getting response from Claude: {e}")
            return None


