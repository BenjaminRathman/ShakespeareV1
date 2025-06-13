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

def append_to_story(filepath, text, is_user=True):
    """Append only new content to the story file"""
    with open(filepath, "a", encoding="utf-8") as f:
        prefix = "User: " if is_user else "Claude: "
        f.write(f"{prefix}{text}\n")
        if is_user:
            f.write("\n")  # Add extra line after user input

def get_story_context(filepath):
    """Read the entire story context from the file"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            # Skip the header (first 3 lines)
            content = f.readlines()
            return "".join(content)
    except Exception as e:
        print(f"Error reading story context: {e}")
        return ""

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
    full_prompt = f"{system_instruction}\n\nStory so far:\n{story_context}\n\nUser: {user_input}" # this part could actually be good because we could make it in the system instructions that if Story so far is empty then it should just be the setting of the story
    
    # Get Claude's response and save it before showing to user
    response = claude.get_response(full_prompt)
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
        full_prompt = f"{system_instruction}\n\nStory so far:\n{story_context}\n\nUser: {user_input}"
        
        # Get and save Claude's response before showing it
        response = claude.get_response(full_prompt)
        append_to_story(story_file, response, is_user=False)
        
        # Now show the response to the user
        print(f"\n{response}")

if __name__ == "__main__":
    main()