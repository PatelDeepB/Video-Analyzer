import cv2
import argparse
import subprocess
import os
from datetime import timedelta

def add_timestamp_to_video(input_path, output_path):
    # Open the video
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {input_path}")
        return
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Define output video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    temp_output = "temp_output.mp4"
    out = cv2.VideoWriter(temp_output, fourcc, fps, (width, height))
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Calculate timestamp
        current_time = frame_count / fps
        timestamp = str(timedelta(seconds=current_time))[:-3]  # Format as MM:SS:MMM
        
        # Add timestamp to frame
        cv2.putText(
            frame,
            timestamp,
            (10, height - 10),  # Bottom-left corner
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),  # White text
            2,
            cv2.LINE_AA
        )
        
        # Write frame to output
        out.write(frame)
        frame_count += 1
    
    # Release resources
    cap.release()
    out.release()
    
    # Convert temporary output to final output with proper encoding
    ffmpeg_cmd = [
        'ffmpeg', '-i', temp_output, '-c:v', 'libx264', '-c:a', 'aac',
        '-strict', 'experimental', output_path
    ]
    subprocess.run(ffmpeg_cmd, check=True)
    
    # Clean up temporary file
    os.remove(temp_output)
    
    print(f"Timestamped video saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add timestamps to a video")
    parser.add_argument("--input", required=True, help="Path to the input video")
    parser.add_argument("--output", default="timestamped_video.mp4", help="Path to the output video")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input video {args.input} not found")
        exit(1)
    
    add_timestamp_to_video(args.input, args.output)
