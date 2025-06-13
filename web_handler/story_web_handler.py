import sys
import os
from datetime import datetime

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from story_controller import create_story_file, append_to_story, get_story_context
from StoryTellerEngine.api_connections import ClaudeAPI
import StoryTellerEngine.system_instructions as system_instructions

class StoryWebHandler:
    def __init__(self):
        self.current_story_file = None
        self.claude = ClaudeAPI()
        self.system_instruction = system_instructions.get_system_instruction()

    def start_story(self):
        """Initialize a new story session"""
        try:
            # Create a new story file
            self.current_story_file = create_story_file()
            
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
            append_to_story(self.current_story_file, user_input)
            
            # Get story context and Claude's response
            story_context = get_story_context(self.current_story_file)
            response = self.claude.get_response(
                system_instruction=self.system_instruction,
                story_context=story_context,
                user_input=user_input
            )
            
            # Save Claude's response
            append_to_story(self.current_story_file, response)
            
            return {
                'success': True,
                'message': response
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Error continuing story: {str(e)}'
            } 