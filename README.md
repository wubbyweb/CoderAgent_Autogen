# CoderAgent_Autogen

## Description
This project demonstrates a multi-agent conversation system using the AutoGen library. It creates a group chat with three agents: a user proxy, an AI assistant, and a coder. The system is designed to help with programming tasks, suggest solutions, and write code to files.

## Features
- Multi-agent conversation system
- Integration with GPT-4 and Anthropic's Claude (Sonnet) models
- Code writing functionality
- Configurable LLM settings

## Requirements
- Python 3.10+
- AutoGen library
- OpenAI API key
- Anthropic API key (optional)

## Installation
1. Clone this repository
2. Install the required packages:
pip install -r requirements.txt

3. Set up your environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `ANTHROPIC_API_KEY`: Your Anthropic API key (if using)

## Usage
Run the main script:
python main.py

The script will initiate a conversation where you can input your programming task. The AI assistant will suggest solutions, and the coder will implement and save the code to files.
## Configuration
You can modify the `llm_config` in `main.py` to adjust settings such as the model, temperature, and seed.
## License
This project is open-source and available under the MIT License.
## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.
## Contact
If you have any questions or feedback, please open an issue in the repository.
