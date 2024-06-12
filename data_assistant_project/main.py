from data_assistant.assistant import DataAssistant

if __name__ == "__main__":
    assistant = DataAssistant("staging_report.csv")
    # assistant.ask_question("Can you provide one insight about flight bookings?")

    while True:
        follow_up = input("Enter your follow-up question (or type 'exit' to stop): !!!")
        if follow_up.lower() == 'exit':
            print("Exiting the follow-up session.")
            break
        assistant.follow_up_question(follow_up)

    # assistant.retrieve_and_handle_run()

