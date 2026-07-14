class Conversation:
    """Represents a conversation between a user and a model."""
    def __init__(self, conversation_id, model):
        self.conversation_id = conversation_id
        self.model = model
        self.messages = []

    def send_message(self, prompt):
        # Generate the model response first
        response = self.model.generate_response(prompt)

        # Store the user message
        self.messages.append({
            "role": "user",
            "content": prompt
        })

        # Store the assistant response
        self.messages.append({
            "role": "assistant",
            "content": response
        })

        return response

    def display_history(self):
        """Display the full conversation history."""
        for message in self.messages:
            print(f"{message['role']}: {message['content']}")
