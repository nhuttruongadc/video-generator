# 🎬 Text to Video Generator

Công cụ tạo video từ văn bản hoàn chỉnh với **âm thanh**, **hình ảnh** và **phụ đề** tự động.

## ✨ Features

- ✅ **Chuyển đổi text thành giọng nói** (Vietnamese, English, và nhiều ngôn ngữ khác)
- ✅ **Tạo hình ảnh động** từ text
- ✅ **Thêm phụ đề tự động** vào video
- ✅ **Kết hợp âm thanh** vào video
- ✅ **Hỗ trợ cả gTTS** (online, chất lượng tốt) **và pyttsx3** (offline, tốc độ nhanh)
- ✅ **Xử lý text tự động** - chia câu hợp lý
- ✅ **Tuỳ chỉnh dễ dàng** - config file đơn giản

## 📦 Installation

### 1. Clone Repository
```bash
git clone https://github.com/nhuttruongadc/video-generator.git
cd video-generator
```

### 2. Cài đặt Dependencies
```bash
pip install -r requirements.txt
```

### 3. Cài đặt FFmpeg (cần thiết)

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download từ https://ffmpeg.org/download.html

## 🚀 Usage

### Cách 1: Chạy Demo
```bash
python main.py
```

### Cách 2: Tạo Video Custom
```python
from utils.video_creator import VideoCreator

creator = VideoCreator()
creator.create_video_from_text(
    "Your text here",
    output_path="output/my_video.mp4"
)
```

### Cách 3: Tạo Video từ File
```python
from utils.video_creator import VideoCreator

creator = VideoCreator()
creator.create_video_from_file(
    "input.txt",
    output_path="output/video.mp4"
)
```

## 🎨 Configuration

Edit `config.py` để tuỳ chỉnh:

```python
CONFIG = {
    'VIDEO_WIDTH': 1280,           # Width của video
    'VIDEO_HEIGHT': 720,           # Height của video
    'FPS': 30,                     # Frames per second
    'FONT_SIZE': 60,               # Kích thước font text
    'FONT_COLOR': (255, 255, 255), # Màu text (RGB)
    'BG_COLOR': (30, 30, 30),      # Màu background
    'AUDIO_LANGUAGE': 'vi',        # Ngôn ngữ (vi, en, fr, etc)
    'AUDIO_SPEED': 150,            # Tốc độ đọc (từ/phút)
    'AUDIO_VOLUME': 0.9            # Âm lượng
}
```

## 📁 Project Structure

```
video-generator/
├── main.py                 # Entry point
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── example_custom.py       # Custom example
├── utils/
│   ├── __init__.py
│   ├── text_processor.py   # Text processing
│   ├── audio_generator.py  # Audio generation (TTS)
│   ├── image_processor.py  # Image creation
│   └── video_creator.py    # Video creation
├── output/                 # Output videos folder
├── assets/                 # Assets (fonts, images)
└── README.md               # Documentation
```

## 🔧 Supported Languages

Hỗ trợ hơn 100 ngôn ngữ thông qua gTTS:
- Vietnamese: `vi`
- English: `en`
- French: `fr`
- Spanish: `es`
- Chinese: `zh-CN`
- Japanese: `ja`
- Korean: `ko`
- Và nhiều ngôn ngữ khác...

## 💡 Tips & Tricks

### 1. Tối ưu hóa Video
```python
# Giảm kích thước file
config.py:
CONFIG['FPS'] = 24  # Thay vì 30
CONFIG['VIDEO_WIDTH'] = 1024
CONFIG['VIDEO_HEIGHT'] = 576
```

### 2. Tăng tốc độ xử lý
```python
# Sử dụng pyttsx3 offline thay vì gTTS online
# Chỉnh AUDIO_SPEED cao hơn
CONFIG['AUDIO_SPEED'] = 200
```

### 3. Batch Processing
```python
import os
from utils.video_creator import VideoCreator

creator = VideoCreator()

for i, file in enumerate(os.listdir('texts/')):
    creator.create_video_from_file(
        f'texts/{file}',
        output_path=f'output/video_{i}.mp4'
    )
```

## ⚠️ Troubleshooting

### Lỗi: "No module named 'moviepy'"
```bash
pip install moviepy
```

### Lỗi: "ffmpeg not found"
Cài đặt FFmpeg (xem phần Installation)

### Âm thanh không hoạt động
```bash
# Cài đặt codec audio
sudo apt-get install ffmpeg libavcodec-extra
```

### Lỗi khi generate âm thanh gTTS
- Kiểm tra kết nối internet
- Script sẽ tự động fallback sang pyttsx3

## 📈 Performance

| Thời gian text | Thời gian xử lý | Output size |
|:--:|:--:|:--:|
| 30 giây | 2-3 phút | 50-100 MB |
| 1 phút | 4-5 phút | 100-150 MB |
| 2 phút | 8-10 phút | 200-300 MB |

*Thời gian có thể khác tùy vào máy và cài đặt*

## 🎯 Use Cases

- 📺 Tạo content YouTube
- 🎓 Video hướng dẫn học tập
- 📝 Đọc sách/bài viết dưới dạng video
- 🎬 Marketing videos
- 📢 Announcement videos
- 🎨 Creative projects

## 📝 License

MIT License - Tự do sử dụng, sửa đổi và phân phối

## 🤝 Contributing

Cảm ơn bạn đã quan tâm! Hãy fork repository và tạo pull request với improvements.

## 📞 Support

Nếu bạn gặp vấn đề, vui lòng:
1. Kiểm tra troubleshooting section
2. Xem GitHub Issues
3. Tạo issue mới với chi tiết về lỗi

---

**Made with ❤️ by nhuttruongadc**
