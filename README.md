# ShakespeareV1 - Interactive AI Storytelling Platform

An immersive interactive storytelling platform powered by Claude AI, featuring both web and voice interfaces for creating dynamic, choice-driven narratives.

## 🎭 Overview

ShakespeareV1 is an interactive storytelling application that combines AI-powered narrative generation with multiple user interfaces. Users can create immersive stories through text input or voice commands, with the AI maintaining story continuity and providing meaningful choices.

## ✨ Features

- **🌐 Web Interface**: Clean, responsive web UI for text-based story interaction
- **🎤 Voice Interface**: Speech-to-text and text-to-speech capabilities for hands-free storytelling
- **🤖 AI-Powered**: Claude AI integration for intelligent, context-aware story generation
- **📚 Story Persistence**: Automatic saving of story sessions with timestamps
- **🎯 Choice-Driven**: Interactive narrative structure with meaningful player choices
- **🔄 Real-time**: Live story updates with immediate AI responses

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Interface │    │  Voice Interface │    │  Story Engine   │
│   (HTML/JS)     │    │  (Speech/TTS)    │    │  (Python)       │
└─────────┬───────┘    └─────────┬────────┘    └─────────┬───────┘
          │                      │                       │
          └──────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────▼─────────────┐
                    │     Flask Server         │
                    │   (API Endpoints)        │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │    Claude AI API         │
                    │  (Story Generation)      │
                    └───────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js (for package management)
- Claude API key from [Anthropic Console](https://console.anthropic.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ShakespeareV1.git
   cd ShakespeareV1
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your Claude API key
   ```

4. **Start the application**
   ```bash
   cd user_interface
   python server.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 🎮 Usage

### Web Interface

1. **Start a Story**: The application automatically initializes when you open the web interface
2. **Describe Setting**: Begin by describing your story's setting, characters, or scenario
3. **Make Choices**: Respond to the AI's prompts with your character's actions
4. **Continue**: The AI will maintain story continuity and present new choices

### Voice Interface

1. **Run Voice Assistant**:
   ```bash
   python UserInteractionHandlers/voice_assistant.py
   ```
2. **Follow Prompts**: Press Enter to start speaking, then Enter again when done
3. **Listen**: The AI will respond through text-to-speech

## 📁 Project Structure

```
ShakespeareV1/
├── StoryTellerEngine/          # Core AI and story logic
│   ├── api_connections.py     # Claude API integration
│   └── system_instructions.py # AI behavior configuration
├── web_handler/               # Web-specific story handling
│   └── story_web_handler.py   # Story state management
├── user_interface/            # Web application
│   ├── index.html            # Main web interface
│   ├── server.py             # Flask web server
│   └── user_interface_files/ # Static assets
├── UserInteractionHandlers/  # Voice and speech components
│   ├── speech_handler.py     # Speech-to-text
│   ├── text_to_speech.py     # Text-to-speech
│   └── voice_assistant.py    # Voice interface
├── stories/                  # Generated story files
├── requirements.txt          # Python dependencies
└── .env.example             # Environment configuration template
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
CLAUDE_API_KEY=your_anthropic_api_key_here
```

### AI Behavior

Modify `StoryTellerEngine/system_instructions.py` to customize:
- Story tone and style
- Choice presentation format
- Character interaction patterns
- Narrative structure

## 🛠️ Development

### Running in Development Mode

```bash
# Start Flask server with debug mode
cd user_interface
python server.py
```

### Adding New Features

1. **New AI Instructions**: Add to `system_instructions.py`
2. **Voice Features**: Extend `UserInteractionHandlers/`
3. **Web Features**: Modify `user_interface/index.html` and `server.py`

## 🐛 Troubleshooting

### Common Issues

**"CLAUDE_API_KEY not found"**
- Ensure your `.env` file exists and contains a valid API key
- Check that the `.env` file is in the project root directory

**"No speech detected"**
- Verify microphone permissions
- Check audio device configuration
- Ensure PyAudio is properly installed

**Web interface not loading**
- Confirm Flask server is running on port 5000
- Check for port conflicts
- Verify all dependencies are installed

### Dependencies

**Python Packages:**
- `anthropic` - Claude AI API client
- `flask` - Web framework
- `flask-cors` - Cross-origin resource sharing
- `speechrecognition` - Speech-to-text
- `pyttsx3` - Text-to-speech
- `pyaudio` - Audio processing
- `python-dotenv` - Environment variable management

## 📝 API Reference

### Web Endpoints

- `POST /start-story` - Initialize a new story session
- `POST /continue-story` - Process user input and continue story
- `GET /` - Serve the main web interface

### Story Handler Methods

- `start_story()` - Create new story session
- `continue_story(user_input)` - Process user input
- `get_story()` - Retrieve current story content
- `get_latest_response()` - Get most recent AI response

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Anthropic](https://www.anthropic.com/) for Claude AI
- [Flask](https://flask.palletsprojects.com/) for web framework
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for voice input

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the API documentation

---

**Happy Storytelling! 🎭✨**
