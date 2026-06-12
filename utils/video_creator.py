from moviepy.editor import (
    ImageClip, AudioFileClip, concatenate_videoclips,
    CompositeVideoClip, ColorClip, TextClip
)
from .text_processor import TextProcessor
from .audio_generator import AudioGenerator
from .image_processor import ImageProcessor
from config import CONFIG
import os
import numpy as np

class VideoCreator:
    """Create videos from text with audio, images, and subtitles"""
    
    def __init__(self):
        self.text_processor = TextProcessor()
        self.audio_generator = AudioGenerator()
        self.image_processor = ImageProcessor()
    
    def create_video_from_text(self, text, output_path=CONFIG['OUTPUT_PATH']):
        """Create complete video from text"""
        print("\n" + "="*60)
        print("🎬 STARTING VIDEO CREATION")
        print("="*60)
        
        try:
            # Step 1: Process text
            print("\n📝 Step 1: Processing text...")
            text = self.text_processor.clean_text(text)
            sentences = self.text_processor.split_text_into_sentences(text)
            print(f"   ✅ Found {len(sentences)} sentences")
            
            clips = []
            audio_files = []
            
            # Step 2: Create clips for each sentence
            print("\n🎨 Step 2: Creating video clips...")
            for i, sentence in enumerate(sentences, 1):
                print(f"\n   [{i}/{len(sentences)}] Processing: {sentence[:60]}...")
                
                # Generate audio
                audio_path = f'temp_audio_{i}.mp3'
                self.audio_generator.text_to_speech_gtts(sentence, audio_path)
                audio_files.append(audio_path)
                
                # Get audio duration
                audio_duration = self.audio_generator.get_audio_duration(audio_path)
                print(f"   ⏱️  Audio duration: {audio_duration:.2f}s")
                
                # Create image with text
                frame = self.image_processor.create_text_image(
                    sentence,
                    CONFIG['VIDEO_WIDTH'],
                    CONFIG['VIDEO_HEIGHT']
                )
                
                # Add subtitle
                frame = self.image_processor.add_subtitle(frame, sentence, position='bottom')
                
                # Create video clip with audio
                video_clip = ImageClip(frame).set_duration(audio_duration)
                audio_clip = AudioFileClip(audio_path)
                video_clip = video_clip.set_audio(audio_clip)
                
                clips.append(video_clip)
            
            # Step 3: Concatenate all clips
            print("\n🔗 Step 3: Concatenating clips...")
            final_video = concatenate_videoclips(clips)
            print(f"   ✅ Total duration: {final_video.duration:.2f}s")
            
            # Step 4: Write to file
            print(f"\n💾 Step 4: Saving video...")
            os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
            
            final_video.write_videofile(
                output_path,
                fps=CONFIG['FPS'],
                codec='libx264',
                audio_codec='aac',
                verbose=False,
                logger=None
            )
            
            # Step 5: Cleanup
            print("\n🧹 Step 5: Cleaning up...")
            for audio_file in audio_files:
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                    print(f"   Removed: {audio_file}")
            
            print("\n" + "="*60)
            print(f"✅ VIDEO CREATED SUCCESSFULLY!")
            print(f"📁 Location: {output_path}")
            print(f"📊 Resolution: {CONFIG['VIDEO_WIDTH']}x{CONFIG['VIDEO_HEIGHT']}")
            print(f"📹 FPS: {CONFIG['FPS']}")
            print("="*60 + "\n")
            
            return output_path
            
        except Exception as e:
            print(f"\n❌ ERROR: {e}")
            raise
    
    def create_video_from_file(self, input_file, output_path=CONFIG['OUTPUT_PATH']):
        """Create video from text file"""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
            return self.create_video_from_text(text, output_path)
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            raise