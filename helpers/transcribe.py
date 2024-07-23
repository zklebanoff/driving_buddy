import assemblyai as aai
from dotenv import load_dotenv
from tempfile import NamedTemporaryFile 
import wave
import os

load_dotenv()
aai.settings.api_key = os.getenv('ASSEMBLYAI_KEY')

transcriber = aai.Transcriber()

def file_transcriber(recorded_audio):
    """
    Transcribes recorded audio and deletes the temporary file after successful submission.

    Args:
        recorded_audio (bytes): The recorded audio data as a byte array.

    Returns:
        str: The transcribed text.
    """

    # Create a temporary file to store the audio data
    with NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_file_path = temp_file.name
        # Write the byte array to a WAV file
        with wave.open(temp_file_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 2 bytes for 16-bit audio
            wf.setframerate(44100)
            wf.writeframes(recorded_audio)

    try:
        # Use AssemblyAI's transcriber object to upload and transcribe
        transcript = transcriber.transcribe(temp_file_path)

        # Extract the transcribed text
        transcript_text = transcript.text
    finally:
        # Delete the temporary file
        os.remove(temp_file_path)

    return transcript_text
