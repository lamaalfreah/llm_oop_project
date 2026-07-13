class PricingPlan:
    def __init__(self, plan_name, price_per_1000_tokens):
        self.plan_name = plan_name
        self.price_per_1000_tokens = price_per_1000_tokens

    def display_plan_info(self):
        return f"Plan Name: {self.plan_name}, Price per 1000 tokens: ${self.price_per_1000_tokens}"

    def calculate_cost(self, tokens):
        return tokens / 1000 * self.price_per_1000_tokens 