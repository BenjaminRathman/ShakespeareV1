from StoryTellerEngine.api_connections import ClaudeAPI
import StoryTellerEngine.system_instructions as system_instructions
from datetime import datetime
import os

def create_story_file():
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

def append_to_story(filepath, text):
    """Append only new content to the story file"""
    with open(filepath, "a", encoding="utf-8") as f:
        # Add separator before each new entry
        f.write("\n\n")
        f.write(f"{text}\n")
        f.write("\n")  # Add extra line after each entry

def get_story_context(filepath):
    """Read the entire story context from the file"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.readlines()
            return "".join(content)
    except Exception as e:
        print(f"Error reading story context: {e}")
        return ""

def create_prompt(system_instruction, story_context, user_input, claude):
    response = claude.get_response(
        system_instruction=system_instruction,
        story_context=story_context,
        user_input=user_input
    )
    return response

def main():
    # Initialize Claude API
    claude = ClaudeAPI()
    system_instruction = system_instructions.get_system_instruction()
    
    # Create story file immediately when program starts
    story_file = create_story_file()
    print(f"Story file created: {story_file}")
    
    print("Start with a setting of your story")
    
    # Get user input and save it immediately
    user_input = input("> ")
    append_to_story(story_file, user_input, is_user=True)
    
    # Get story context and create full prompt
    story_context = get_story_context(story_file)
    #full_prompt = create_prompt(system_instruction, story_context, user_input, claude)
    
    # Get Claude's response and save it before showing to user
    response = claude.get_response(
    system_instruction=system_instruction,
    story_context=story_context,
    user_input=user_input
    )
    append_to_story(story_file, response, is_user=False)
    
    # Now show the response to the user
    print(f"\n{response}")
    
    # Continue the conversation loop
    while True:
        user_input = input("\nYour choice (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        # Save user input immediately
        append_to_story(story_file, user_input, is_user=True)
        
        # Get story context and create full prompt
        story_context = get_story_context(story_file)
        #full_prompt = create_prompt(system_instruction, story_context, user_input, claude)
        
        # Get and save Claude's response before showing it
        response = claude.get_response(
        system_instruction=system_instruction,
        story_context=story_context,
        user_input=user_input
        )
        append_to_story(story_file, response, is_user=False)
        
        # Now show the response to the user
        print(f"\n{response}")

if __name__ == "__main__":
    main()