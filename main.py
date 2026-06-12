#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text to Video Generator - Main Script
Convert text to complete video with audio, images, and subtitles
"""

from utils.video_creator import VideoCreator
import os

def main():
    """Main function to create video from text"""
    
    # Sample Vietnamese text
    sample_text = """
    Xin chào, đây là video được tạo tự động từ văn bản.
    Video này có âm thanh, hình ảnh và phụ đề rất hoàn chỉnh.
    Bạn có thể thay đổi nội dung văn bản để tạo video khác.
    Công nghệ này rất hữu ích để tạo nội dung cho YouTube.
    Hay cũng có thể dùng để tạo video hướng dẫn học tập.
    Với công cụ này, bạn có thể tự động hóa quá trình tạo video.
    Hãy thử sử dụng và tạo ra những video tuyệt vời nhất.
    """
    
    print("\n" + "#"*60)
    print("#" + " "*58 + "#")
    print("#" + "  Text to Video Generator - Demo".center(58) + "#")
    print("#" + " "*58 + "#")
    print("#"*60)
    
    # Create video
    creator = VideoCreator()
    
    try:
        output_file = creator.create_video_from_text(
            sample_text,
            output_path='output/video.mp4'
        )
        
        print(f"\n🎉 SUCCESS! Video created at: {output_file}\n")
        
        # Check if file exists
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file) / (1024 * 1024)  # Convert to MB
            print(f"📊 File size: {file_size:.2f} MB")
        
    except Exception as e:
        print(f"\n❌ Failed to create video: {e}\n")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())