# Video to Audio Converter

This script converts videos in a specified folder to MP3 audio format using FFmpeg.

## Prerequisites

- Python 3.x
- FFmpeg installed and accessible in the system's PATH

## Installation

1. Clone or download the script to your local machine.

2. Install the required dependencies by running the following command:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python video_to_mp3.py <folder> [bitrate]
```
- `<folder>`: Path to the folder containing the videos.
- `[bitrate]` (optional): Audio bitrate for the output MP3 files. Default is '256k'.

Example usage:
```bash
python video_to_mp3.py /path/to/videos 192k
```


## Features

- Supports conversion of various video formats (mp4, avi, mov, mkv, flv, wmv, webm) to MP3.
- Option to specify the audio bitrate for the output MP3 files.

## Troubleshooting

- If you encounter any issues during the conversion process, ensure that FFmpeg is installed and accessible in the system's PATH.

## License

- The Video to Audio Converter script is licensed under **...**

- FFmpeg, the underlying multimedia framework used for the conversion, is distributed under the [GNU Lesser General Public License (LGPL)](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) version 2.1 or later.

Please ensure that you comply with the terms of the respective licenses when using or distributing this software.
