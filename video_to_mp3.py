import os
import subprocess
import sys

DEFAULT_BITRATE = "256k"

def convert_videos_to_mp3(folder, bitrate=DEFAULT_BITRATE):
    """
    Convert videos in a folder to MP3 audio format.

    Args:
        folder (str): Path to the folder containing the videos.
        bitrate (str, optional): Audio bitrate for the output MP3 files. Default is '256k'.

    Returns:
        None
    """
    # Check if the folder exists
    if not os.path.isdir(folder):
        print("The specified folder does not exist.")
        return

    # Iterate through files in the folder
    for file in os.listdir(folder):
        if file.endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm')):
            # Get the full path of input and output files
            input_file = os.path.join(folder, file)
            output_file = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')

            # Conversion using FFmpeg
            cmd = ['ffmpeg', '-i', input_file, '-vn', '-acodec', 'libmp3lame', '-ab', bitrate, output_file]
            subprocess.call(cmd)

    print("Conversion completed!")

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Utilisation : python {__name__}.py <dossier> [bitrate]")
    else:
        folder = sys.argv[1]
        bitrate = sys.argv[2] if len(sys.argv) == 3 else DEFAULT_BITRATE
        convert_videos_to_mp3(folder, bitrate)
