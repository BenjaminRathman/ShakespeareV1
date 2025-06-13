import webbrowser
import os
import sys

def open_browser():
    try:
        # Get the absolute path to the index.html file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, 'index.html')
        
        # Verify the file exists
        if not os.path.exists(html_path):
            print(f"Error: Could not find index.html at {html_path}")
            return
            
        # Convert to file URL format
        file_url = 'file:///' + html_path.replace('\\', '/')
        print(f"Opening: {file_url}")
        
        # Open in default browser
        webbrowser.open(file_url)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    open_browser() 