# 🎬 GUI Application - Hướng dẫn sử dụng

## ✨ Tính năng

Giao diện đồ họa đơn giản, **không cần Terminal** - chỉ cần:
1. Nhập text
2. Click **"CREATE VIDEO"**
3. Chờ video hoàn thành ✅

## 📥 Cách sử dụng (Dễ nhất)

### Bước 1: Download
Vào https://github.com/nhuttruongadc/video-generator → **Code** → **Download ZIP**

### Bước 2: Giải nén
- Chuột phải file ZIP → **Extract All**
- Chọn nơi lưu (Desktop hoặc Documents)

### Bước 3: Cài dependencies (1 lần duy nhất)
Mở **Command Prompt** hoặc **PowerShell** trong folder `video-generator-main`:

```bash
pip install -r requirements.txt
```

### Bước 4: Cài FFmpeg (QUAN TRỌNG!)

**Windows:**
```bash
choco install ffmpeg
```
Nếu không có choco, cài từ: https://chocolatey.org/install

**Mac:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

### Bước 5: Chạy GUI Application

**Windows:**
- Double-click file `gui_app.py` hoặc
- Gõ trong Command Prompt: `python gui_app.py`

**Mac/Linux:**
```bash
python3 gui_app.py
```

## 🎨 Giao diện ứng dụng

```
┌─────────────────────────────────────────┐
│  🎬 Text to Video Generator             │
├─────────────────────────────────────────┤
│                                         │
│  📝 Nhập văn bản (Text Input):          │
│  ┌─────────────────────────────────┐   │
│  │ Xin chào, đây là video được tạo │   │
│  │ tự động từ văn bản...           │   │
│  │                                 │   │
│  └─────────────────────────────────┘   │
│                                         │
│  📌 Load Sample Text                   │
│                                         │
│  ⚙️ Options                            │
│  🌐 Language: ⦿ Tiếng Việt ◯ English  │
│  📺 Resolution: ⦿ 720p ◯ 1080p       │
│                                         │
│  🎬 CREATE VIDEO  📁 Open Folder       │
│                                         │
│  ✓ Ready                                │
└─────────────────────────────────────────┘
```

## 📝 Cách sử dụng

### 1. Nhập text
- Click vào ô text
- Gõ hoặc dán nội dung bạn muốn

### 2. Chọn ngôn ngữ
- 🇻🇳 Tiếng Việt (mặc định)
- 🇬🇧 English
- 🇫🇷 Français

### 3. Chọn chất lượng video
- **720p (Fast)** - Tạo nhanh, file nhỏ
- **1080p (Better)** - Chất lượng tốt, file lớn

### 4. Click "🎬 CREATE VIDEO"
- Ứng dụng sẽ bắt đầu tạo video
- Thanh progress hiển thị trạng thái
- Chờ đến khi hoàn thành ✅

### 5. Video hoàn thành!
- File được lưu ở thư mục `output/`
- Click "📁 Open Folder" để xem video

## ⏱️ Thời gian xử lý

| Độ dài text | Thời gian |
|:---:|:---:|
| 30 giây | 2-3 phút |
| 1 phút | 4-5 phút |
| 2 phút | 8-10 phút |

*Thời gian tùy thuộc vào máy tính của bạn*

## 📁 Output

Video được lưu tại: `output/video_YYYYMMDD_HHMMSS.mp4`

Ví dụ: `output/video_20260612_143022.mp4`

## ⚠️ Troubleshooting

### Lỗi: "No module named 'tkinter'"
- **Windows**: Cài lại Python, tick vào "tcl/tk and IDLE"
- **Mac**: `brew install python-tk@3.11`
- **Linux**: `sudo apt-get install python3-tk`

### Lỗi: "ffmpeg not found"
- Cài FFmpeg (xem Bước 4 ở trên)

### Lỗi: "No audio generated"
- Kiểm tra kết nối internet (gTTS cần internet)
- Hoặc cài pyttsx3: `pip install pyttsx3`

### Video tạo rất chậm
- Thay đổi Resolution thành 720p
- Hoặc đợi thêm một chút (bình thường mất 2-5 phút)

## 💡 Tips

1. **Sample Text**: Click "📌 Load Sample Text" để thử với ví dụ
2. **Văn bản dài**: Để ứng dụng hoạt động tốt, tách thành nhiều đoạn
3. **Cải thiện chất lượng**: Dùng 1080p nhưng mất thời gian hơn
4. **Batch processing**: Chạy tuần tự, không chạy nhiều cái cùng lúc

## 🎯 Ví dụ sử dụng

### Ví dụ 1: Tiếng Việt
```
Xin chào, đây là video tạo tự động.
Công nghệ này rất hữu ích.
Hãy thử sử dụng!
```

### Ví dụ 2: English
```
Hello, this is an automated video.
You can create videos from text.
Just paste your text and click create!
```

### Ví dụ 3: Content Creator
```
Hôm nay tôi sẽ hướng dẫn bạn cách tạo video tự động.
Bước 1: Chuẩn bị nội dung text.
Bước 2: Mở ứng dụng.
Bước 3: Dán text vào.
Bước 4: Click tạo video.
Video sẽ được tạo tự động!
```

## ✅ Checklist trước khi sử dụng

- [ ] Đã download và giải nén repository
- [ ] Đã cài Python 3.7+ (với tkinter)
- [ ] Đã cài FFmpeg
- [ ] Đã chạy: `pip install -r requirements.txt`
- [ ] Đã chạy: `python gui_app.py`
- [ ] Giao diện xuất hiện trên màn hình

## 🆘 Cần giúp?

Nếu gặp vấn đề:
1. Kiểm tra troubleshooting ở trên
2. Xem README.md
3. Tạo issue trên GitHub

---

**Happy video creating! 🎬✨**
