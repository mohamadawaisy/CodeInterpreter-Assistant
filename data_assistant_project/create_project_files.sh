#!/bin/bash

# Create project root directory
mkdir -p data_assistant_project
cd data_assistant_project || exit

# Create directories
mkdir -p data_assistant tests saved_messages

# Create empty Python files in data_assistant
touch data_assistant/__init__.py
touch data_assistant/assistant.py
touch data_assistant/config_manager.py
touch data_assistant/logger.py
touch data_assistant/openai_client.py

# Create empty Python files in tests
touch tests/__init__.py
touch tests/test_assistant.py
touch tests/test_config_manager.py

# Create other necessary files
touch run_id.txt
touch assistant_config.json
touch assistant_log.txt
touch main.py
touch requirements.txt

# Add initial content to requirements.txt
echo "openai" > requirements.txt

echo "Project structure created successfully."
