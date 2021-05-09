import en_core_web_sm
from typing import List
from ..utils import generate_sentences

class Tokenizer:

    def __init__(self, nlp=None, min_sen_len=3):
        self.min_sen_len = min_sen_len
        self.default_nlp = nlp or en_core_web_sm.load()

    def to_sentences(self, text: str) -> List[str]:
        return generate_sentences(text, self.default_nlp, min_sen_len=self.min_sen_len)

    @staticmethod
    def to_words(sentence: str) -> List[str]:
        return [w.strip() for w in sentence.split(" ")]

