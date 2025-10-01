# 🎵 YouTube Music Downloader - Modern UI

A sleek, modern YouTube music downloader with a beautiful fluent design interface. Download individual songs or entire playlists with an intuitive, user-friendly experience.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## Quick Start

#### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

#### Installation

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install system dependencies**
   
   **Windows:**
   - Download [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases) and add to PATH
   - Download [FFmpeg](https://ffmpeg.org/download.html) and add to PATH

   
   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt update
   sudo apt install python3-pip ffmpeg
   pip3 install yt-dlp
   ```

3. **Run the application**
   ```bash
   python final.py
   ```

### Dependencies
- **Python 3.8+** (for source installation)
- **yt-dlp**: YouTube video/audio downloader
- **FFmpeg**: Audio processing library
- **CustomTkinter**: Modern UI framework

### Supported URL Formats
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://music.youtube.com/watch?v=VIDEO_ID`
- `https://www.youtube.com/playlist?list=PLAYLIST_ID`
- `https://music.youtube.com/playlist?list=PLAYLIST_ID`

## 🛠️ Troubleshooting

### Common Issues

**❌ "yt-dlp: Not found" error**
- **Solution**: Install yt-dlp using `pip install yt-dlp` or download from [releases](https://github.com/yt-dlp/yt-dlp/releases)

**❌ "FFmpeg: Not found" error**
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
- **macOS**: Run `brew install ffmpeg`
- **Linux**: Run `sudo apt install ffmpeg`

**❌ Download fails with "Video unavailable"**
- **Solution**: Check if the video is region-locked or private. Try updating yt-dlp: `pip install --upgrade yt-dlp`

**❌ Application won't start**
- **Solution**: Ensure Python 3.8+ is installed and all dependencies are met
- Try running: `pip install --upgrade -r requirements.txt`

### Performance Tips
- **Close other applications** during large downloads
- **Use wired internet** for better stability
- **Choose SSD storage** for faster file writing
- **Download during off-peak hours** for better speeds

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/yourusername">Botiwa</a></p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>