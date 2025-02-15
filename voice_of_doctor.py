from dotenv import load_dotenv
load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is AI with SPK!"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

#Step2: Use Model for Text output to Voice

from gtts import gTTS
import subprocess
import platform
from playsound import playsound

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    # Generate audio file with gTTS
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    # Get the operating system
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            playsound(output_filepath)  # Play MP3 file on Windows
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # Use a suitable player
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# Test the function
input_text = "Hi, this is AI with SPK, autoplay testing!"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")



import os
import platform
import subprocess
from playsound import playsound
from elevenlabs import ElevenLabs

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  # Make sure your API key is set in the environment variables

    # Create the ElevenLabs client
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    # Generate the audio using ElevenLabs
    audio_generator = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    # Save the audio file
    with open(output_filepath, "wb") as audio_file:
        for chunk in audio_generator:  # Write each chunk of audio data
            audio_file.write(chunk)

    # Determine the operating system
    os_name = platform.system()
    try:
        # Handle audio playback based on the operating system
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            playsound(output_filepath)  # Use playsound for MP3 playback on Windows
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # Use mpg123 for Linux MP3 playback
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Test the function
# text_to_speech_with_elevenlabs(
#     input_text="Hello! This is a test of ElevenLabs text-to-speech playback.",
#     output_filepath="elevenlabs_testing_autoplay.mp3"
# )
