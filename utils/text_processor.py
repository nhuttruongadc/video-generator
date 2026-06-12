import re

class TextProcessor:
    """Process and split text into manageable chunks"""
    
    @staticmethod
    def split_text_into_sentences(text, max_words=15):
        """Split text into sentences with maximum words per sentence"""
        sentences = re.split(r'[.!?]+', text)
        result = []
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            
            words = sentence.split()
            if len(words) <= max_words:
                result.append(sentence)
            else:
                # Split long sentences
                for i in range(0, len(words), max_words):
                    chunk = ' '.join(words[i:i+max_words])
                    if chunk.strip():
                        result.append(chunk)
        
        return result
    
    @staticmethod
    def clean_text(text):
        """Clean and normalize text"""
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        return text
    
    @staticmethod
    def estimate_reading_time(text):
        """Estimate reading time in seconds (assuming 150 words per minute)"""
        words = len(text.split())
        minutes = words / 150
        return minutes * 60