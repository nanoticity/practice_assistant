# Script to generate OGG audio files for specific phrases using gTTS and pydub
from gtts import gTTS
from pydub import AudioSegment
import os

def generate_ogg(word, output_dir="sounds"):
    # Create sounds directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate temporary MP3 using gTTS
    temp_mp3 = "temp.mp3"
    tts = gTTS(text=word, lang='en')
    tts.save(temp_mp3)
    
    name = word.replace(" ", "_")
    
    # Convert MP3 to OGG
    audio = AudioSegment.from_mp3(temp_mp3)
    output_file = os.path.join(output_dir, f"{name}.ogg")
    audio.export(output_file, format="ogg")
    
    # Clean up temporary MP3
    os.remove(temp_mp3)
    print(f"Generated: {output_file}")

# Example usage
if __name__ == "__main__":
    words = ["negative one", 
             "negative two", 
             "negative three", 
             "negative four",
             "negative five",
             "one",
             "two",
             "three",
             "half speed",
             "reset",
             "done next phrase",]
    for word in words:
        generate_ogg(word)

