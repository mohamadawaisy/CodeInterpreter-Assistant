# CodeInterpreter-Assistant

This repository is a proof-of-concept integration of OpenAI's Assistant and Code Interpreter APIs. It provides the capability to create an assistant, manage threads, and run code, allowing users to ask questions with follow-up inquiries about a data file.

## Features

- **Assistant Creation**: Set up an AI assistant tailored to your needs.
- **Thread Management**: Create and manage execution threads for interactive sessions.
- **Code Execution**: Run code snippets and handle data file queries interactively.
- **Follow-Up Questions**: Ask sequential questions about a data file, enhancing the interactivity.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/mohamadawaisy/CodeInterpreter-Assistant.git
    cd CodeInterpreter-Assistant
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `config.json` file in the root directory with your OpenAI API key:

    ```json
    {
        "openai_api_key": "your_openai_api_key"
    }
    ```

## Usage

1. Import the `DataAssistant` class:

    ```python
    from data_assistant_project import DataAssistant
    ```

2. Initialize the `DataAssistant`:

    ```python
    assistant = DataAssistant(config_path='config.json')
    ```

3. Create an assistant and manage threads:

    ```python
    # Create a thread
    thread_id = assistant.create_thread()

    # Upload a file
    assistant.upload_file(thread_id, 'example.py')

    # Execute code and ask questions
    result = assistant.execute_code(thread_id, 'print("Hello, World!")')
    print(result)

    # Follow-up question
    follow_up = assistant.ask_follow_up(thread_id, 'Can you process the data in example.py?')
    print(follow_up)
    ```

## Contributing

Contributions are welcome! Fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue in this repository.

