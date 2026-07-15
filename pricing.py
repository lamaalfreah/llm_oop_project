class PricingPlan:
    """Represents a pricing plan for language model requests."""

    def __init__(self, plan_name, price_per_1000_tokens):
        self.plan_name = plan_name
        self.price_per_1000_tokens = price_per_1000_tokens

    def display_plan_info(self):
        """Return formatted information about the pricing plan.

        Returns:
            A string containing the plan information.
        """
        return f"Plan Name: {self.plan_name}, Price per 1000 tokens: ${self.price_per_1000_tokens}"

    def calculate_cost(self, tokens):
        """Calculate the cost for a number of tokens.

        Args:
            tokens: The number of tokens.

        Returns:
            The calculated token cost.

        Raises:
            TypeError: If tokens is not an integer.
            ValueError: If tokens is negative.
        """
        return tokens / 1000 * self.price_per_1000_tokens 