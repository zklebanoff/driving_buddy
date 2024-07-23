import sounddevice as sd
from helpers.transcribe import file_transcriber
from helpers.record import record_audio
from helpers.anthropic_helpers.messages import Messages
from helpers.anthropic_helpers.claude_chat import chat_with_claude
from helpers.anthropic_helpers.tools.process_tool_calls import process_tool_call
from helpers.clean_output import clean_output
from helpers.text_to_speech import text_to_speech_file

def main():
    """
    The main function for recording, transcribing, and deleting audio files.

    Runs a loop for repeated recording sessions with start, stop, and quit commands.
    """
    messages = Messages()

    # Main loop for recording sessions
    while True:
        user_input = input("Enter 's' to start recording, 'q' to exit: ").lower()

        if user_input == 's':
            
            recorded_audio = record_audio() # Record audio 
            transcript = file_transcriber(recorded_audio) # Transcribe

            print(transcript) # USER INPUT
            messages.add_message('user',transcript)

            resp = chat_with_claude(messages.get_messages())

            messages.add_message(resp.role, resp.content)


            # TOOL USE
            while resp.stop_reason == "tool_use":
                tool_content = process_tool_call(resp)
                print(tool_content)
                messages.add_message('user', [tool_content])
                print(messages.get_messages())
                resp = chat_with_claude(messages.get_messages())
                messages.add_message(resp.role, resp.content)
            
            # OUTPUT
            final_response = clean_output(resp)

            print("FINAL RESPONSE")
            print(final_response)
            # Text to speech
            # text_to_speech_file(final_response)
            
            # Save the transcript to a file (optional)
            # with open("transcript.txt", "w") as f:
            #     f.write(transcript)

        elif user_input == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid command. Please enter 's' to start recording or 'quit' to exit.")

if __name__ == "__main__":
    main()
