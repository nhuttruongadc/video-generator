from PIL import Image, ImageDraw, ImageFont
import numpy as np
from config import CONFIG
import os

class ImageProcessor:
    """Process and create images for video"""
    
    @staticmethod
    def get_font(font_size=CONFIG['FONT_SIZE']):
        """Load font, fallback to default if not found"""
        font_paths = [
            'assets/fonts/Arial.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux
            '/System/Library/Fonts/Arial.ttf',  # macOS
            'C:\\Windows\\Fonts\\arial.ttf',  # Windows
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    return ImageFont.truetype(font_path, font_size)
                except:
                    continue
        
        return ImageFont.load_default()
    
    @staticmethod
    def create_text_image(text, width=CONFIG['VIDEO_WIDTH'], height=CONFIG['VIDEO_HEIGHT']):
        """Create image with text"""
        # Create background
        img = Image.new('RGB', (width, height), color=CONFIG['BG_COLOR'])
        draw = ImageDraw.Draw(img)
        
        # Load font
        font = ImageProcessor.get_font(CONFIG['FONT_SIZE'])
        
        # Calculate text position (center)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (width - text_width) // 2
        y = (height - text_height) // 2 - 50
        
        # Draw text with shadow effect
        shadow_offset = 3
        draw.text((x + shadow_offset, y + shadow_offset), text, fill=(50, 50, 50), font=font)
        draw.text((x, y), text, fill=CONFIG['FONT_COLOR'], font=font)
        
        return np.array(img)
    
    @staticmethod
    def load_background_image(path, width=CONFIG['VIDEO_WIDTH'], height=CONFIG['VIDEO_HEIGHT']):
        """Load and resize background image"""
        try:
            img = Image.open(path).convert('RGB')
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            return np.array(img)
        except Exception as e:
            print(f"   ⚠️  Could not load background image: {e}")
            return None
    
    @staticmethod
    def add_subtitle(frame, text, position='bottom'):
        """Add subtitle to frame"""
        img = Image.fromarray(frame.astype('uint8'))
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Load font
        font = ImageProcessor.get_font(40)
        
        # Calculate text position
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        if position == 'bottom':
            x = (img.width - text_width) // 2
            y = img.height - text_height - 40
        else:
            x = (img.width - text_width) // 2
            y = 20
        
        # Draw semi-transparent background
        padding = 10
        draw.rectangle(
            [(x - padding, y - padding), 
             (x + text_width + padding, y + text_height + padding)],
            fill=(0, 0, 0, 200)
        )
        
        # Draw text
        draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
        
        return np.array(img)
    
    @staticmethod
    def create_gradient_background(width=CONFIG['VIDEO_WIDTH'], height=CONFIG['VIDEO_HEIGHT'], 
                                  color1=(30, 30, 30), color2=(60, 60, 60)):
        """Create gradient background image"""
        img = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(img)
        
        for y in range(height):
            ratio = y / height
            r = int(color1[0] + (color2[0] - color1[0]) * ratio)
            g = int(color1[1] + (color2[1] - color1[1]) * ratio)
            b = int(color1[2] + (color2[2] - color1[2]) * ratio)
            
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        
        return np.array(img)