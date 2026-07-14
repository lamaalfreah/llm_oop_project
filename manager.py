from models import LanguageModel
class ModelManager:
    """Manages a collection of language models."""
    def __init__(self):
        self.models = {}

    def add_model(self, model):
        """Add a language model to the manager.

        Args:
            model: The language model to add.

        Raises:
            TypeError: If model is not a LanguageModel.
            DuplicateModelError: If the model name already exists.
        """
        if isinstance(model, LanguageModel):
            self.models[model.model_name] = model
        else:
            raise TypeError("Only instances of LanguageModel can be added.")

    def get_model(self, model_name):
        """Return a model using its name.

        Args:
            model_name: The name of the requested model.

        Returns:
            The matching language model.

        Raises:
            ModelNotFoundError: If the model does not exist.
        """
        return self.models.get(model_name)

       
    def list_models(self):
        """Display the names of all registered models."""
        for model_name in self.models:
            print(model_name)

    def remove_model(self, model_name):
        """Remove a model using its name.

        Args:
            model_name: The name of the model to remove.

        Raises:
            ModelNotFoundError: If the model does not exist.
        """
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