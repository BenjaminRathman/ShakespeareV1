from api_connections import ClaudeAPI

def get_claude_response():
    """
    Get a response from Claude based on user input
    """
    try:
        # Initialize Claude API
        claude = ClaudeAPI()
        
        while True:
            # Get user input
            print("\nEnter your prompt (or 'quit' to exit):")
            prompt = input("> ")
            
            # Check if user wants to quit
            if prompt.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            # Get response from Claude
            print("\nGetting response from Claude...")
            response = claude.get_response(prompt)
            
            if response:
                print("\nClaude's response:")
                print("-" * 50)
                print(response)
                print("-" * 50)
            else:
                print("Sorry, I couldn't get a response from Claude.")
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Claude Interface!")
    print("Type your prompt and press Enter to get a response from Claude.")
    print("Type 'quit' to exit.")
    get_claude_response() 