from models import LanguageModel
class ModelManager:
    def __init__(self):
        self.models = {}

    def add_model(self, model):
        if isinstance(model, LanguageModel):
            self.models[model.model_name] = model
        else:
            raise TypeError("Only instances of LanguageModel can be added.")

    def get_model(self, model_name):
        return self.models.get(model_name)

       
    def list_models(self):
        for model_name in self.models:
            print(model_name)

    def remove_model(self, model_name):
        if model_name in self.models:
            del self.models[model_name]

    def select_model(self, provider, required_tokens):
        suitable_models = []

        for model in self.models.values():
            if (
                model.provider == provider
                and model.max_tokens >= required_tokens
                and model.is_active
            ):
                suitable_models.append(model)

        if not suitable_models:
            return None

        return min(
            suitable_models,
            key=lambda model: model.max_tokens
        )