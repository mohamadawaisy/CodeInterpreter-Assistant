import openai
import os
from datetime import datetime

class OpenAIClient:
    def __init__(self):
        self.client = openai.OpenAI()

    def upload_file(self, file_path):
        return self.client.files.create(
            file=open(file_path, "rb"),
            purpose='assistants'
        )

    def create_assistant(self, file_id):
        return self.client.beta.assistants.create(
            name="ASSISTANT data API",
            instructions="You are a helpful assistant; you answer questions based on data and provide charts and graphs to support your answers and insights.",
            tools=[{"type": "code_interpreter"}],
            tool_resources={"code_interpreter": {"file_ids": [file_id]}},
            model="gpt-4o",
        )

    def create_thread(self):
        return self.client.beta.threads.create()

    def process_question(self, thread_id, assistant_id, question):
        self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=question
        )

        return self.client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )

    def display_responses(self, run, logger, run_dir):
        if run.status == 'completed':
            logger.log("Run completed successfully. Processing messages.")
            messages = self.client.beta.threads.messages.list(thread_id=run.thread_id)
            for msg in messages.data:
                if msg.role == "assistant":
                    for content_item in msg.content:
                        if content_item.type == 'text':
                            text_value = content_item.text.value
                            if content_item.text.annotations:
                                for annotation in content_item.text.annotations:
                                    if annotation.type == 'file_path':
                                        file_id = annotation.file_path.file_id
                                        logger.log(f"Attempting to download file with ID: {file_id}")
                                        file_data = self.client.files.content(file_id)
                                        file_path = os.path.join(run_dir, f"{file_id}.csv")
                                        with open(file_path, "wb") as file:
                                            file.write(file_data.read())
                                        text_value += f"\nDownloaded CSV file: {file_path}"
                            response = f"Assistant says: {text_value}"
                            logger.log(response)
                            # Save the response to a file
                            response_file = os.path.join(run_dir, f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
                            with open(response_file, 'w') as file:
                                file.write(response)
                        elif content_item.type == 'image_file':
                            file_id = content_item.image_file.file_id
                            logger.log(f"Attempting to download image file with ID: {file_id}")
                            file_data = self.client.files.content(file_id)
                            file_path = os.path.join(run_dir, f"{file_id}.png")
                            with open(file_path, "wb") as file:
                                file.write(file_data.read())
                            response = f"Assistant says: Saved image file to {file_path}"
                            logger.log(response)
                            # Save the response to a file
                            response_file = os.path.join(run_dir, f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
                            with open(response_file, 'w') as file:
                                file.write(response)
                        else:
                            response = "Assistant says: Unhandled content type."
                            logger.log(response)
                            # Save the response to a file
                            response_file = os.path.join(run_dir, f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
                            with open(response_file, 'w') as file:
                                file.write(response)
                else:
                    response = f"User says: {msg.content}"
                    logger.log(f"Processing user message: {response}")
                    # Save the response to a file
                    response_file = os.path.join(run_dir, f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
                    with open(response_file, 'w') as file:
                        file.write(response)

    def retrieve_run_steps(self, thread_id, run_id):
        return self.client.beta.threads.runs.steps.list(thread_id=thread_id, run_id=run_id)
