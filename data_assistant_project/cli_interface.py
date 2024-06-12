from data_assistant.assistant import DataAssistant
from data_assistant.config_manager import ConfigManager
class DataAssistantCLI:
    """
    Command-line interface for interacting with the Data Assistant.
    """
    
    def __init__(self):
        self.default_name = "Data Helper"
        self.default_instruction = "You are a helpful assistant; you answer questions based on data and provide charts and graphs to support your answers and insights."
        self.config_manager = ConfigManager()
    
    def get_user_input(self):
            """
            Prompts the user for assistant name and instruction, with defaults.
            """
            if self.config_manager.config_exists():
                use_existing = input("Configuration exists. Do you want to use the existing configuration? (y/n): ").strip().lower()
                if use_existing == 'y':
                    print("Using existing configuration.")
                    return None
                else:
                    self.config_manager.remove_config()
                    print("Creating new configuration.")

            print(f"Default assistant name: {self.default_name}")
            assistant_name = input("Enter the name of the assistant (or press Enter to accept the default): ").strip() or self.default_name

            print(f"Default instruction: {self.default_instruction}")
            assistant_instruction = input("Enter the instruction for the assistant (or press Enter to accept the default): ").strip() or self.default_instruction

            return assistant_name, assistant_instruction

    def run(self):
        """
        Runs the main loop for user interaction.
        """
        assistant_name, assistant_instruction = self.get_user_input()
        assistant = DataAssistant("sample_data.xlsx", assistant_name, assistant_instruction)

        while True:
            follow_up = input("Enter your follow-up question (or type 'exit' to stop): ").strip()
            if follow_up.lower() == 'exit':
                print("Exiting the follow-up session.")
                break
            assistant.follow_up_question(follow_up)
