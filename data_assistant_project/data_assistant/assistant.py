from .openai_client import OpenAIClient
from .config_manager import ConfigManager
from .logger import Logger
import os
import json
from datetime import datetime

class DataAssistant:
    def __init__(self, file_path, base_dir="assistants", log_file="assistant_log.txt"):
        self.file_path = file_path
        self.base_dir = base_dir
        self.log_file = log_file
        self.logger = Logger()
        self.config_manager = ConfigManager()
        self.client = OpenAIClient()
        self.assistant_dir = None
        self.run_dir = None
        self.file = None
        self.assistant = None
        self.thread = None

        self.initialize_assistant()

    def initialize_assistant(self):
        if self.config_manager.config_exists():
            self.config = self.config_manager.load_from_file()
            self.file = type('obj', (object,), {'id': self.config['file_id']})
            self.assistant = type('obj', (object,), {'id': self.config['assistant_id']})
            self.thread = type('obj', (object,), {'id': self.config['thread_id']})
            self.assistant_dir = os.path.join(self.base_dir, f"assistant_{self.assistant.id}")
            self.logger.set_log_file(os.path.join(self.assistant_dir, "assistant_log.txt"))
        else:
            self.setup_new_assistant()

    def setup_new_assistant(self):
        try:
            self.file = self.upload_file(self.file_path)
            self.assistant = self.create_assistant()
            self.thread = self.create_thread()
            self.assistant_dir = os.path.join(self.base_dir, f"assistant_{self.assistant.id}")
            os.makedirs(self.assistant_dir, exist_ok=True)
            self.logger.set_log_file(os.path.join(self.assistant_dir, "assistant_log.txt"))
            self.config_manager.save_to_file(self.file.id, self.assistant.id, self.thread.id)
        except Exception as e:
            self.logger.log(f"Initialization failed: {e}")
            self.thread = None

    def upload_file(self, file_path):
        return self.client.upload_file(file_path)

    def create_assistant(self):
        return self.client.create_assistant(self.file.id)

    def create_thread(self):
        return self.client.create_thread()

    def ask_question(self, question):
        if not self.thread:
            self.logger.log_error("Thread not initialized properly.")
            return

        try:
            run = self.process_question(question)
            self.run_dir = os.path.join(self.assistant_dir, f"run_{run.id}")
            os.makedirs(self.run_dir, exist_ok=True)
            self.logger.set_log_file(os.path.join(self.run_dir, "run_log.txt"))
            question_file = os.path.join(self.run_dir, f"question_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
            with open(question_file, 'w') as file:
                file.write(question)
            with open(os.path.join(self.run_dir, "run_id.txt"), "w") as file:
                file.write(run.id)
            self.logger.log(f"Run ID {run.id} saved in {self.run_dir}.")
            self.client.display_responses(run, self.logger, self.run_dir)
        except Exception as e:
            self.logger.log_error(f"Failed to ask question: {e}")

    def follow_up_question(self, question):
        self.ask_question(question)

    def process_question(self, question):
        return self.client.process_question(self.thread.id, self.assistant.id, question)

    def retrieve_and_handle_run(self):
        try:
            with open(os.path.join(self.run_dir, "run_id.txt"), "r") as file:
                run_id = file.read().strip()
            self.logger.log(f"Retrieved Run ID: {run_id}")

            run_steps = self.client.retrieve_run_steps(self.thread.id, run_id)
            self.client.display_responses(run_steps, self.logger, self.run_dir)
        except Exception as e:
            self.logger.log_error(f"Failed to retrieve and handle run: {str(e)}")
