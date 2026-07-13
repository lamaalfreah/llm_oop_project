from tokenizer import Tokenizer
from exceptions import InvalidPromptError
class LanguageModel:
    total_models = 0
    def __init__(self, model_name, provider, max_tokens, temperature, pricing_plan, is_active= True):
        self.model_name = model_name
        self.provider = provider
        self.max_tokens = max_tokens
        self.temperature = temperature
        LanguageModel.total_models += 1 
        self.tokenizer = Tokenizer()
        self.pricing_plan = pricing_plan  # Aggregation: reference passed from outside
        self.__is_active = is_active

    def validate_prompt(self, prompt):
        if not isinstance(prompt, str):
            raise InvalidPromptError("Prompt must be a string.")

        if not prompt.strip():
            raise InvalidPromptError("Prompt cannot be empty.")
    
    def generate_response(self, prompt):
        self.validate_prompt(prompt)
        return f"{self.model_name} response to: '{prompt}\nInput tokens: {self.tokenizer.count_tokens(prompt)}'"
    
    def display_info(self):
        return f"Model Name: {self.model_name}, Provider: {self.provider}, Max Tokens: {self.max_tokens}, Temperature: {self.temperature}"

    @classmethod
    def get_total_models(cls):
        return cls.total_models
    
    @staticmethod
    def validate_temperature(temperature):
        return 0.0 <= temperature <= 2.0
    
    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        """Setter for temperature with boundary validation."""
        if not (0 <= value <= 2):
            raise ValueError("Temperature must be between 0 and 2.")
        self.__temperature = value

    def calculate_request_cost(self, prompt):
        token_count = self.tokenizer.count_tokens(prompt)
        cost = self.pricing_plan.calculate_cost(token_count)

        print(f"Tokens: {token_count}")
        print(f"Estimated Cost: ${cost:.6f}")
    
    def __str__(self):
        return f"{self.model_name} by {self.provider}"
    
    def __repr__(self):
        return f"model_name={self.model_name}, provider={self.provider})"

    def __len__(self):
        return self.max_tokens

    def __eq__(self, other):
        return (self.model_name == other.model_name and 
                self.provider == other.provider)

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_active must be True or False.")

        self.__is_active = value

class GPTModel(LanguageModel, LoggingMixin):
    def __init__(self, model_name, provider, max_tokens, temperature, api_key, pricing_plan, is_active=True):
        super().__init__(model_name, provider, max_tokens, temperature, pricing_plan, is_active)
        self.api_key = api_key

    def generate_response(self, prompt):
        self.validate_prompt(prompt)
        LoggingMixin.log(self, "Sending request to GPT-Model")
        return f"GPT API response to: '{prompt}\nInput tokens: {self.tokenizer.count_tokens(prompt)}'"
    
class LlamaModel(LanguageModel):
    def __init__(self, model_name, provider, max_tokens, temperature, model_path, quantization, pricing_plan, is_active=True):
        super().__init__(model_name, provider, max_tokens, temperature, pricing_plan, is_active)
        self.model_path = model_path
        self.quantization = quantization

    def generate_response(self, prompt):
        self.validate_prompt(prompt)
        return f"Local Llama response to: '{prompt}\nInput tokens: {self.tokenizer.count_tokens(prompt)}'"

class LoggingMixin:
    def log(self, message):
        print(f"[LOG]: {message}")