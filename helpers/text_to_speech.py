from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os
import uuid
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

load_dotenv()

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech_file(text: str) -> str:
    """
    Converts text to speech and saves the output as a temporary MP3 file.

    This function uses a specific client for text-to-speech conversion. It configures
    various parameters for the voice output and saves the resulting audio stream to a
    temporary MP3 file.

    Args:
        text (str): The text content to convert to speech.

    Returns:
        str: The file path of the temporary audio file.
    """
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Create a temporary file to write the audio stream
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_file_path = temp_file.name
        for chunk in response:
            if chunk:
                temp_file.write(chunk)

    print(f"A new audio file was saved temporarily at {temp_file_path}")

    # Return the path of the temporary audio file
    return temp_file_path


if __name__ == "__main__":
    temp_file_path = text_to_speech_file("Waddup fam!")
    try:
        # Example usage:
        audio = AudioSegment.from_file(temp_file_path)
        play(audio)
    finally:
        # Clean up: Delete the temporary file after use
        os.remove(temp_file_path)
        print(f"Temporary audio file {temp_file_path} has been deleted.")
