from flask import Flask, request, jsonify
from data_assistant.assistant import DataAssistant
from data_assistant.config_manager import ConfigManager

app = Flask(__name__)

class DataAssistantAPI:
    """
    REST API interface for interacting with the Data Assistant.
    """
    
    def __init__(self):
        self.default_name = "Data Helper"
        self.default_instruction = "You are a helpful assistant; you answer questions based on data and provide charts and graphs to support your answers and insights."
        self.config_manager = ConfigManager()
        self.assistant = None
    
    def create_assistant(self, name=None, instruction=None):
        """
        Creates a Data Assistant instance.
        """
        if self.config_manager.config_exists():
            return "Configuration exists. Use the existing configuration or delete it to create a new one."

        assistant_name = name or self.default_name
        assistant_instruction = instruction or self.default_instruction
        self.assistant = DataAssistant("sample_data.xlsx", assistant_name, assistant_instruction)
        return "Assistant created successfully"
    
    def follow_up_question(self, question):
        """
        Handles follow-up questions.
        """
        if not self.config_manager.config_exists():
            return "Assistant not created. Please create the assistant first."
        self.assistant = DataAssistant("sample_data.xlsx", "", "")
        return self.assistant.follow_up_question(question)
    
    def reset_configuration(self):
        """
        Resets the configuration by removing the existing config.
        """
        self.config_manager.remove_config()
        self.assistant = None
        return "Configuration reset successfully."

api_interface = DataAssistantAPI()

@app.route('/create_assistant', methods=['POST'])
def create_assistant():
    data = request.json
    name = data.get('name')
    instruction = data.get('instruction')
    message = api_interface.create_assistant(name, instruction)
    return jsonify({"message": message}), 201 if "successfully" in message else 200

@app.route('/follow_up', methods=['POST'])
def follow_up():
    data = request.json
    question = data.get('question')
    response = api_interface.follow_up_question(question)
    return jsonify({"response": response}), 200

@app.route('/reset_config', methods=['POST'])
def reset_config():
    message = api_interface.reset_configuration()
    return jsonify({"message": message}), 200

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(debug=True)
