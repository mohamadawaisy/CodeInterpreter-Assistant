# AI Assistant with OpenAI

This repository contains the code for building and deploying an AI Assistant using OpenAI's API, which includes capabilities for processing and analyzing data with a powerful code interpreter. This AI Assistant is designed to interact with backend systems, providing data-driven insights and automated responses based on natural language queries.

## Features

- **AI Assistant Initialization**: Set up an AI assistant that can execute code, analyze data, and provide actionable insights.
- **Data File Management**: Upload and manage files directly through the OpenAI API, allowing the AI to work with specific datasets.
- **Advanced Data Analysis**: Use the code interpreter tool to process data queries and return results including diagrams, charts, and CSV files.
- **Logging and Error Handling**: Incorporate sophisticated logging for debugging and monitoring the assistant’s operations.

## Getting Started

### Prerequisites

- Python 3.8 or later
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
    from data_assistant.assistant import DataAssistant
    ```

2. Initialize the `DataAssistant`:

    ```python
    assistant = DataAssistant("path_to_your_data_file.csv")
    ```

3. Interact with the AI Assistant:

    ```python
    # Ask a question
    response = assistant.ask_question("What insights can you provide about recent sales data?")
    print(response)

    # Follow-up question
    follow_up_question = "Can you break down the sales by product category?"
    follow_up_response = assistant.follow_up_question(follow_up_question)
    print(follow_up_response)

    # Advanced Data Analysis
    analysis_result = assistant.ask_question("Generate a sales forecast for the next quarter.")
    print(analysis_result)
    ```

## Contributing

Contributions are welcome! Fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please open an issue on the GitHub repository.

Project Link: [https://github.com/mohamadawaisy/CodeInterpreter-Assistant](https://github.com/mohamadawaisy/CodeInterpreter-Assistant)

Article: https://medium.com/@mr.ma.swi/a-step-by-step-guide-with-openais-assistant-and-code-interpreter-ac19d07af9e0

