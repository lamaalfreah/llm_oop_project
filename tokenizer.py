class Tokenizer:
    """Provides simple tokenization functionality."""
    def __init__(self):
        pass
        
    def count_tokens(self, text):
        """Count the number of tokens in a text.

        Args:
            text: The text whose tokens will be counted.

        Returns:
            The number of tokens.
        """
        return len(self.tokenize(text))
    
    def tokenize(self, text):
        """Split text into tokens using whitespace.

        Args:
            text: The text to tokenize.

        Returns:
            A list containing the text tokens.

        Raises:
            TypeError: If text is not a string.
        """
        return text.split()