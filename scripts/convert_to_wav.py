import os
import subprocess

INPUT_DIR = "audio_raw"
OUTPUT_DIR = "audio_clean"

def convert_audio(input_path, output_path):
    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-ac", "1",
        "-ar", "16000",
        output_path
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.wav', '.mp3', '.m4a', '.flac', '.aac', '.ogg')):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".wav"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            print(f"Converting {filename} → {output_filename}")
            convert_audio(input_path, output_path)

if __name__ == "__main__":
    main()
