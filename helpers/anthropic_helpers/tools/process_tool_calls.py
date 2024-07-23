from helpers.anthropic_helpers.tools.navigate import navigate_tool

def process_tool_call(message):
    tool_use = next(block for block in message.content if block.type == "tool_use")
    tool_name = tool_use.name
    tool_input = tool_use.input
    tool_obj = {
        "tool_use_id": tool_use.id,
        "type": "tool_result",
    }

    if tool_name == "navigate":
        tool_obj["content"] = navigate_tool(tool_input["locations"])
        return tool_obj