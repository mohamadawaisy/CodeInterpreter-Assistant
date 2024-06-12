import argparse
import subprocess

class Main:
    """
    Main execution class to run either CLI or API interface.
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Data Assistant Interface")
        self.parser.add_argument('--mode', choices=['cli', 'api'], default='api', help="Mode to run the assistant: 'cli' for command-line interface, 'api' for REST API")
        self.parser.add_argument('--prod', action='store_true', help="Run the API in production mode using gunicorn")

    def run(self):
        args = self.parser.parse_args()
        mode = args.mode

        if mode == 'cli':
            from cli_interface import DataAssistantCLI
            cli = DataAssistantCLI()
            cli.run()
        elif mode == 'api':
            if args.prod:
                # Run the API using gunicorn
                subprocess.run(['gunicorn', '-w', '4', '-b', '127.0.0.1:8080', 'api_interface:app'])
            else:
                from api_interface import app
                app.run(debug=True)
        else:
            print("Invalid mode selected. Please choose 'cli' or 'api'.")

if __name__ == "__main__":
    main = Main()
    main.run()
