import autogen
import os

# Configure the LLM
config_list = [
    {
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY"),
    },
    {
        "model": "sonnet",
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
    }
]

llm_config = {
    "config_list": config_list,
    "seed": 42,
    "temperature": 0
}

# Create agents
user_proxy = autogen.UserProxyAgent(
    name="User_Proxy",
    system_message="A human user who needs help with a programming task.",
    code_execution_config={"work_dir": "coding"}
)

assistant = autogen.AssistantAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. You can analyze problems and suggest solutions.",
    llm_config=llm_config
)

coder = autogen.AssistantAgent(
    name="Coder",
    system_message="You are an expert Python programmer. Your task is to take code suggestions, check for any errors, correct it and and write them to files in the work directory.",
    llm_config=llm_config
)

def write_code_to_file(filename: str, code: str, work_dir: str):
    file_path = os.path.join(work_dir, filename)
    with open(file_path, 'w') as file:
        file.write(code)
    return f"Code written to {file_path}"

coder.register_function(
    function_map={
        "write_code_to_file": write_code_to_file
    }
)

# Create a group chat
groupchat = autogen.GroupChat(agents=[user_proxy, assistant, coder], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Start the conversation
user_proxy.initiate_chat(
    manager,
    message="""I need help creating a Python function that converts a string list to comma seperate string. 
    Once the Assistant suggests the code, the Coder should write it to a file named 'list2string.py' in the work directory."""
)
