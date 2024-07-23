import re

def remove_thinking_tags(input_string):
    pattern = r'<thinking>.*?</thinking>'
    return re.sub(pattern, '', input_string)

def clean_output(resp):
    final_response = next((block.text for block in resp.content if hasattr(block, "text")),None,)
    return remove_thinking_tags(final_response)
            