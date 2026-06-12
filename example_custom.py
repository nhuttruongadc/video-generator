#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom Example - Create video from your own text
"""

from utils.video_creator import VideoCreator

def create_custom_video():
    """Create video from custom text"""
    
    # Your custom text here
    your_text = """
    Đây là video custom của bạn.
    Bạn có thể viết bất kỳ nội dung gì bạn muốn.
    Công cụ sẽ tự động tạo video với âm thanh và phụ đề.
    """
    
    creator = VideoCreator()
    creator.create_video_from_text(
        your_text,
        output_path='output/custom_video.mp4'
    )

if __name__ == "__main__":
    create_custom_video()