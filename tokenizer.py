class Tokenizer:
    def __init__(self):
        pass
        
    def count_tokens(self, text):
        return len(self.tokenize(text))
    
    def tokenize(self, text):
        return text.split()