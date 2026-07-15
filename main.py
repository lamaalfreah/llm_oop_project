from models import LanguageModel, GPTModel, LlamaModel
from pricing import PricingPlan
from conversation import Conversation
from manager import ModelManager
from tokenizer import Tokenizer
from exceptions import InvalidPromptError

#Only for testing purposes
def main():
    pricing = PricingPlan(
        plan_name="Standard",
        price_per_1000_tokens=0.02
    )

    model = LanguageModel(
        model_name="Basic-LLM",
        provider="Local",
        max_tokens=2048,
        temperature=0.7,
        pricing_plan=pricing
    )

    print(model.display_info())
    response = model.generate_response(
        "Explain artificial intelligence"
    )
    print(response)

    model1 = LanguageModel(
        model_name="Basic-LLM",
        provider="Local",
        max_tokens=2048,
        temperature=0.7,
        pricing_plan=pricing
    )
    model2 = LanguageModel(
        model_name="Basic-LLM",
        provider="Local",
        max_tokens=2048,
        temperature=0.7, 
        pricing_plan=pricing
    )
    model3 = LanguageModel(
        model_name="Basic-LLM",
        provider="Local",
        max_tokens=2048,
        temperature=0.7,
        pricing_plan=pricing
    )

    print(LanguageModel.total_models)
    print(LanguageModel.get_total_models())
    print(LanguageModel.validate_temperature(0.7))
    print(LanguageModel.validate_temperature(3.5))
    model.temperature = 1.2
    # model.temperature = 4

    gpt = GPTModel(
        model_name="GPT-Model",
        provider="OpenAI",
        max_tokens=4096,
        temperature=0.7,
        api_key="secret-key",
        pricing_plan=pricing
    )

    llama = LlamaModel(
        model_name="Llama-Model",
        provider="Local",
        max_tokens=8192,
        temperature=0.5,
        model_path="/models/llama",
        quantization="4-bit",
        pricing_plan=pricing
    )

    print(gpt.generate_response("What is Python?"))
    print(llama.generate_response("What is Python?"))


    #Apply Polymorphism
    models = [gpt, llama]
    for model in models:
        print(model.generate_response("Explain OOP"))

    tokenizer = Tokenizer()

    tokens = tokenizer.count_tokens(
        "Artificial intelligence is powerful"
    )
    print(tokens)

    gpt = GPTModel(
        model_name="GPT-Model",
        provider="OpenAI",
        max_tokens=4096,
        temperature=0.7,
        api_key="secret-key",
        pricing_plan=pricing
    )

    print(len(gpt))

    gpt.calculate_request_cost(
        "Artificial intelligence is powerful"
    )
    print(model1 == model2)
    print(gpt.__repr__())

    try:
        print(gpt.generate_response(""))
    except InvalidPromptError as error:
        print(error)

    conversation = Conversation(
        conversation_id=1,
        model=gpt
    )

    conversation.send_message("What is artificial intelligence?")
    conversation.send_message("Explain machine learning.")

    conversation.display_history()

    print(conversation.messages)

    try:
        conversation.send_message("")
    except InvalidPromptError as error:
        print(error)

    print(len(conversation.messages))

    manager = ModelManager()

    manager.add_model(gpt)
    manager.add_model(llama)

    manager.list_models()

    selected_model = manager.get_model("GPT-Model")
    print(selected_model)
    manager.remove_model("GPT-Model")
    manager.list_models()

    manager = ModelManager()

    manager.add_model(gpt)
    manager.add_model(llama)

    selected_model = manager.select_model(
        provider="OpenAI",
        required_tokens=3000
    )

    print(selected_model)

    selected_model = manager.select_model(
        provider="OpenAI",
        required_tokens=5000
    )

    print(selected_model)

    gpt.is_active = False

    selected_model = manager.select_model(
        provider="OpenAI",
        required_tokens=1000
    )

    print(selected_model)


if __name__ == "__main__":
    main()