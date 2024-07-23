# Driving Buddy

Driving Buddy is a Proof of Concept (POC) application that provides voice-activated directions between two locations using Google Maps API. It leverages various technologies to create a seamless voice-to-voice experience for getting driving directions.

## Features

- Voice input for specifying start and end locations
- Audio transcription of voice input
- Natural language processing to extract location information
- Integration with Google Maps API for route information
- Text-to-speech output for driving directions

## How It Works

1. The user starts a recording session with a voice command.
2. The application records the user's voice input.
3. The audio is transcribed to text.
4. Anthropic's Claude AI is used to process the transcribed text and extract location information.
5. The location data is sent to Google Maps API to retrieve directions.
6. Claude AI is used again to format the directions into natural language.
7. The formatted directions are converted to speech using ElevenLabs' text-to-speech technology.
8. The audio response is played back to the user.

## Technologies Used

- Python
- sounddevice: For audio recording
- Google Speech-to-Text API: For audio transcription
- Anthropic's Claude AI: For natural language processing and understanding
- Google Maps API: For retrieving directions
- ElevenLabs API: For text-to-speech conversion

## Future Improvements

While this is a small POC, there are several potential improvements that could be made:

1. Integrate real-time traffic information
2. Add weather forecasts for the route and destination
3. Implement a RAG (Retrieval-Augmented Generation) bot to suggest fun activities at the destination
4. Enhance the voice interface for a more interactive experience
5. Add support for multiple languages
6. Implement error handling and edge cases for more robust performance