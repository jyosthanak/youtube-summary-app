# YouTube Summary Generator 🎥

A powerful Chrome browser extension that generates AI-powered summaries of YouTube videos instantly. Perfect for quickly understanding video content without watching the entire video.

## Features ✨

### 🚀 **Core Functionality**
- **One-Click Summaries** - Generate AI summaries of any YouTube video
- **Real-time Processing** - Get summaries in seconds
- **Clean Interface** - Simple, intuitive popup design
- **Error Handling** - Robust error reporting and status updates

### 🎯 **User Experience**
- **Minimal Permissions** - Only requires activeTab and scripting permissions
- **Lightweight** - Fast loading and minimal resource usage
- **Visual Feedback** - Clear status indicators and loading states
- **Read-Only Display** - Clean textarea for easy reading and copying

### 🔧 **Technical Features**
- **Manifest V3** - Uses the latest Chrome extension standards
- **Local Server Integration** - Connects to local AI processing server
- **JSON API** - Clean REST API communication
- **Cross-Origin Support** - Proper CORS handling

## Installation 📦

### Prerequisites
- Google Chrome browser
- Local backend server running on port 5000 (see Backend Setup below)

### Chrome Extension Installation

**Method 1: Developer Mode (Recommended)**
1. Download or clone this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" in the top right corner
4. Click "Load unpacked" and select the extension folder
5. The extension will appear in your Chrome toolbar

**Method 2: Manual Installation**
1. Download the extension files
2. Go to `chrome://extensions/`
3. Drag and drop the extension folder onto the page

## Backend Setup 🔧

This extension requires a local backend server to process YouTube videos and generate summaries.

### Required Server Endpoints

**POST /summarize**
```json
{
  "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

**Response Format:**
```json
{
  "summary": "AI-generated summary of the video content..."
}
```

### Server Requirements
- **Port:** 5000 (http://127.0.0.1:5000)
- **CORS:** Must allow requests from Chrome extension
- **Content-Type:** application/json

### Example Server Implementation (Python Flask)
```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize_video():
    data = request.get_json()
    youtube_url = data.get('youtube_url')
    
    # Your AI summarization logic here
    summary = generate_summary(youtube_url)
    
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
```

## Usage 🎯

1. **Start Backend Server**
   - Ensure your local server is running on port 5000
   - Server should be accessible at `http://127.0.0.1:5000`

2. **Navigate to YouTube**
   - Open any YouTube video in Chrome
   - The video should be fully loaded

3. **Generate Summary**
   - Click the extension icon in your Chrome toolbar
   - Click "Summarize This Video" button
   - Wait for the AI to process the video (usually 5-15 seconds)

4. **Read Summary**
   - The summary will appear in the text area
   - Copy the summary if needed
   - Close the popup when done

## File Structure 📁

```
youtube_extension/
├── manifest.json          # Extension configuration
├── popup.html            # Extension popup interface
├── popup.js              # Frontend JavaScript logic
├── popup.js.json         # Configuration file
├── popup.json.js         # Additional config
├── popup.txt             # Documentation/notes
└── README.md             # This file
```

## Permissions 🔐

The extension requests minimal permissions:

- **activeTab** - Access the current YouTube video URL
- **scripting** - Inject scripts to interact with YouTube pages
- **host_permissions** - Connect to local backend server (127.0.0.1:5000)

## Technical Details 🛠️

### Architecture
- **Frontend**: Chrome Extension (Manifest V3)
- **Backend**: Local HTTP server (Python Flask recommended)
- **Communication**: REST API with JSON payloads
- **Processing**: AI-powered video summarization

### API Flow
1. User clicks "Summarize" button
2. Extension gets current tab URL
3. URL sent to local server via POST request
4. Server processes video and generates summary
5. Summary returned to extension and displayed

### Error Handling
- Network connection errors
- Invalid YouTube URLs
- Server unavailable scenarios
- Empty or malformed responses

## Development 💻

### Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/jyosthanak/youtube-summary-app.git
cd youtube-summary-app

# Load extension in Chrome
# 1. Go to chrome://extensions/
# 2. Enable Developer mode
# 3. Click "Load unpacked"
# 4. Select the extension folder
```

### Testing
1. Start your local backend server
2. Load the extension in Chrome
3. Navigate to a YouTube video
4. Test the summarization feature
5. Check browser console for any errors

### Debugging
- Open Chrome DevTools for the extension popup
- Check Network tab for API requests
- Review Console for JavaScript errors
- Verify server logs for backend issues

## Troubleshooting 🔍

### Common Issues

**"Error fetching summary"**
- Ensure backend server is running on port 5000
- Check if CORS is properly configured
- Verify the server endpoint is accessible

**"Empty response"**
- Backend server might not be returning proper JSON
- Check server logs for processing errors
- Verify the YouTube URL is valid

**Extension not loading**
- Refresh the extension in chrome://extensions/
- Check for manifest.json syntax errors
- Verify all required files are present

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Built with Chrome Extension Manifest V3
- Designed for seamless YouTube integration
- AI-powered summarization capabilities

---

**Made with ❤️ for better video consumption**