# 🎥 Video Logo Detection Project

This project uses the Gemini API to detect logos in a video through frame-by-frame analysis. It identifies the exact timestamps, durations, and descriptions of logo appearances, making it ideal for analyzing branded content in videos. The project includes scripts to add timestamps to videos, process the video with the Gemini API, and store results in a structured JSON format.

---

## ✨ Features

- **Logo Detection**: Detects intentional logo appearances in videos with precise timestamps.
- **Frame-by-Frame Analysis**: Analyzes every frame to ensure no logo is missed.
- **Timestamp Overlay**: Adds visible timestamps to videos for easier verification.
- **Structured Output**: Saves results in JSON format for further analysis.
- **Gemini API Integration**: Leverages Google's Gemini API for advanced video analysis.

---

## 🧰 Requirements

See `requirements.txt` for the full list of dependencies. Key requirements include:

- Python 3.10  
- Google Gemini API key (set as `GEMINI_API_KEY` environment variable)  
- FFmpeg (for video processing)

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/video-logo-detection.git
cd video-logo-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

- **Windows**: Download from the FFmpeg website and add it to your PATH.  
- **macOS**:  
  ```bash
  brew install ffmpeg
  ```  
- **Linux**:  
  ```bash
  sudo apt-get install ffmpeg
  ```

### 4. Set Up Gemini API Key

- Obtain a Gemini API key from Google Cloud Console.  
- Set the environment variable:  
  ```bash
  export GEMINI_API_KEY='your-api-key'
  ```

### 5. Prepare a Video

- Place a video file (e.g., `input_video.mp4`) in the project directory.

---

## ▶️ Usage

### Add Timestamps to Video

```bash
python add_timestamp.py --input input_video.mp4 --output timestamped_video.mp4
```

### Run Logo Detection

```bash
python detect_logos.py --video timestamped_video.mp4
```

### View Results

- Results are saved in `logo_detection_results.json` in the project directory.

---

## 📁 Files

- `README.md`: Project overview and instructions.  
- `requirements.txt`: Python dependencies.  
- `prompt.txt`: Prompt used for Gemini API logo detection.  
- `detect_logos.py`: Script to detect logos using the Gemini API.  
- `add_timestamp.py`: Script to add timestamps to the video.  
- `logo_detection_results.json`: Output file containing logo detection results.

---

## 🧪 Example Output

Example structure of `logo_detection_results.json`:

```json
[
    {
        "start_time": "00:02:500",
        "end_time": "00:06:000",
        "duration": "00:03:500",
        "brand_name": "Nike",
        "description": "Nike logo displayed prominently on a banner.",
        "is_repeated": false
    }
]
```

---

## 🤝 Contributing

Feel free to submit issues or pull requests to improve the project. Contributions are welcome!

---

## 📜 License

This project is licensed under the MIT License.

