import json
import os

class ConfigManager:
    def __init__(self, config_file="assistant_config.json"):
        self.config_file = config_file

    def config_exists(self):
        return os.path.exists(self.config_file)

    def save_to_file(self, file_id, assistant_id, thread_id):
        with open(self.config_file, 'w') as f:
            json.dump({
                'file_id': file_id,
                'assistant_id': assistant_id,
                'thread_id': thread_id
            }, f)

    def load_from_file(self):
        with open(self.config_file, 'r') as f:
            return json.load(f)
