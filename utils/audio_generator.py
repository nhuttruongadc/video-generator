from gtts import gTTS
import pyttsx3
import os
from config import CONFIG

class AudioGenerator:
    """Generate audio from text using text-to-speech"""
    
    def __init__(self, language=CONFIG['AUDIO_LANGUAGE']):
        self.language = language
        self.use_gtts = True  # Try gTTS first (online, better quality)
    
    def text_to_speech_gtts(self, text, output_path='temp_audio.mp3'):
        """Convert text to speech using gTTS (Google Text-to-Speech)"""
        try:
            print(f"   🔊 Generating audio with gTTS...")
            tts = gTTS(text=text, lang=self.language, slow=False)
            tts.save(output_path)
            return output_path
        except Exception as e:
            print(f"   ⚠️  gTTS failed: {e}. Trying pyttsx3...")
            return self.text_to_speech_pyttsx3(text, output_path)
    
    def text_to_speech_pyttsx3(self, text, output_path='temp_audio.mp3'):
        """Convert text to speech using pyttsx3 (offline engine)"""
        try:
            print(f"   🔊 Generating audio with pyttsx3...")
            engine = pyttsx3.init()
            engine.setProperty('rate', CONFIG['AUDIO_SPEED'])
            engine.setProperty('volume', CONFIG['AUDIO_VOLUME'])
            engine.save_to_file(text, output_path)
            engine.runAndWait()
            return output_path
        except Exception as e:
            print(f"   ❌ Error generating audio: {e}")
            raise
    
    def get_audio_duration(self, audio_path):
        """Get audio duration in seconds"""
        try:
            from moviepy.editor import AudioFileClip
            audio = AudioFileClip(audio_path)
            duration = audio.duration
            audio.close()
            return duration
        except Exception as e:
            print(f"   ⚠️  Error getting audio duration: {e}")
            return 3.0  # Default fallback
    
    def generate_silence(self, duration=1.0, output_path='silence.mp3'):
        """Generate silence audio file"""
        try:
            from pydub import AudioSegment
            silence = AudioSegment.silent(duration=int(duration*1000))
            silence.export(output_path, format="mp3")
            return output_path
        except:
            return None