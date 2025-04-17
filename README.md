# Video Logo Detection Project

This project uses the Gemini API to detect logos in a video through frame-by-frame analysis. It identifies the exact timestamps, durations, and descriptions of logo appearances, making it ideal for analyzing branded content in videos. The project includes scripts to add timestamps to videos, process the video with the Gemini API, and store results in a structured JSON format.

## Features
- **Logo Detection**: Detects intentional logo appearances in videos with precise timestamps.
- **Frame-by-Frame Analysis**: Analyzes every frame to ensure no logo is missed.
- **Timestamp Overlay**: Adds visible timestamps to videos for easier verification.
- **Structured Output**: Saves results in JSON format for further analysis.
- **Gemini API Integration**: Leverages Google's Gemini API for advanced video analysis.

## Requirements
See `requirements.txt` for the full list of dependencies. Key requirements include:
- Python 3.8+
- Google Gemini API key (set as `GEMINI_API_KEY` environment variable)
- FFmpeg (for video processing)

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/video-logo-detection.git
   cd video-logo-detection
