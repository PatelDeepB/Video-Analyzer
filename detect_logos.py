import base64
import json
import os
import argparse
from google import genai
from google.genai import types

def read_prompt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def detect_logos(video_path, prompt_path):
    # Initialize Gemini API client
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    # Upload video file
    with open(video_path, 'rb') as video_file:
        video_data = video_file.read()
    video_file_name = os.path.basename(video_path)
    uploaded_file = client.files.upload(file=video_file_name, content=video_data)
    
    # Read prompt
    prompt_text = read_prompt(prompt_path)
    
    # Set up content for API request
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=uploaded_file.uri,
                    mime_type=uploaded_file.mime_type,
                ),
                types.Part.from_text(text=prompt_text),
            ],
        ),
    ]
    
    # Configure API settings
    generate_content_config = types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_CIVIC_INTEGRITY",
                threshold="BLOCK_LOW_AND_ABOVE",
            ),
        ],
        response_mime_type="text/plain",
    )
    
    # Stream API response and collect results
    result_text = ""
    for chunk in client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=contents,
        config=generate_content_config,
    ):
        result_text += chunk.text
    
    # Parse JSON result
    try:
        results = json.loads(result_text)
    except json.JSONDecodeError:
        results = []
    
    # Save results to JSON file
    output_file = "logo_detection_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)
    
    print(f"Logo detection results saved to {output_file}")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect logos in a video using Gemini API")
    parser.add_argument("--video", required=True, help="Path to the input video file")
    parser.add_argument("--prompt", default="prompt.txt", help="Path to the prompt file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.video):
        print(f"Error: Video file {args.video} not found")
        exit(1)
    
    if not os.path.exists(args.prompt):
        print(f"Error: Prompt file {args.prompt} not found")
        exit(1)
    
    detect_logos(args.video, args.prompt)
