import sys
import os
from datetime import datetime

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from StoryTellerEngine.api_connections import ClaudeAPI
import StoryTellerEngine.system_instructions as system_instructions

class StoryWebHandler:
    def __init__(self):
        self.current_story_file = None
        self.claude = ClaudeAPI()
        self.system_instruction = system_instructions.get_system_instruction()
        self.latest_response = None

    def create_story_file(self):
        """Create a new story file with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"story_{timestamp}.txt"
        
        # Create the stories directory if it doesn't exist
        if not os.path.exists("stories"):
            os.makedirs("stories")
        
        filepath = os.path.join("stories", filename)
        
        # Create the file and write initial header
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Story Session Started: {timestamp}\n")
            f.write("=" * 50 + "\n\n")
        
        return filepath

    def append_to_story(self, text):
        """Append only new content to the story file"""
        with open(self.current_story_file, "a", encoding="utf-8") as f:
            # Add separator before each new entry
            f.write("\n\n")
            f.write(f"{text}\n")
            f.write("\n")  # Add extra line after each entry

    def get_story_context(self):
        """Read the entire story context from the file"""
        try:
            with open(self.current_story_file, "r", encoding="utf-8") as f:
                content = f.readlines()
                return "".join(content)
        except Exception as e:
            print(f"Error reading story context: {e}")
            return ""

    def start_story(self):
        """Initialize a new story session"""
        try:
            # Create a new story file
            self.current_story_file = self.create_story_file()
            
            return {
                'success': True,
                'message': "Welcome! Please describe the setting for your story.",
                'story_file': self.current_story_file
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error starting story: {str(e)}'
            }

    def get_story(self):
        """Get the current story content"""
        try:
            if not self.current_story_file:
                return {
                    'success': False,
                    'message': 'No active story session'
                }

            story_content = self.get_story_context()
            return {
                'success': True,
                'content': story_content
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error getting story: {str(e)}'
            }

    def continue_story(self, user_input):
        """Process user input and continue the story"""
        try:
            if not self.current_story_file:
                return {
                    'success': False,
                    'message': 'No active story session'
                }

            if not isinstance(user_input, str):
                return {
                    'success': False,
                    'message': 'Input must be a string'
                }

            # Clean the input
            user_input = user_input.strip()
            if not user_input:
                return {
                    'success': False,
                    'message': 'Input cannot be empty'
                }

            # Save user input
            self.append_to_story(user_input)
            
            # Get story context and Claude's response
            story_context = self.get_story_context()
            response = self.claude.get_response(
                system_instruction=self.system_instruction,
                story_context=story_context,
                user_input=user_input
            )
            
            # Save Claude's response
            self.append_to_story(response)
            self.latest_response = response
            
            return {
                'success': True,
                'message': response
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error continuing story: {str(e)}'
            }

    def get_latest_response(self):
        """Get the latest response from Claude"""
        try:
            if not self.latest_response:
                return {
                    'success': False,
                    'message': 'No response available'
                }
            
            return {
                'success': True,
                'response': self.latest_response
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error getting response: {str(e)}'
            } 