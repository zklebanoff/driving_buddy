import sounddevice as sd
import numpy as np

def record_audio():
    """
    Records audio from the microphone until interrupted by Enter.

    Returns:
        bytes: The recorded audio data as a byte array.
    """

    recorded_data = []

    def callback(indata, frames, time, status):
        recorded_data.append(indata.copy())

    # Set audio recording parameters
    fs = 44100  # Increased sample rate for better quality
    channels = 1

    # Start recording with a callback
    with sd.InputStream(samplerate=fs, channels=channels, callback=callback):
        print("Press Enter to stop recording.")
        while True:
            try:
                # Check for Enter key press
                if input().strip() == "":
                    print("Recording stopped.")
                    break
                sd.sleep(100)
            except KeyboardInterrupt:
                # Handle potential keyboard interrupts (optional)
                print("Recording interrupted.")
                break

    # Concatenate recorded chunks into a single array
    audio_data = np.concatenate(recorded_data, axis=0)

    # Normalize audio data
    audio_data = audio_data / np.max(np.abs(audio_data))

    # Convert the NumPy array to a byte array
    audio_bytes = (audio_data * 32767).astype(np.int16).tobytes()

    return audio_bytes
