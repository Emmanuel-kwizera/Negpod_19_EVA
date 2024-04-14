from dataclasses import dataclass


@dataclass
class Meter:
    meter_id: str
    nickname: str
    tokens: dict

    def add_token(self, token, amount):
        self.tokens[token] = amount

    def get_tokens(self):
        return self.tokens
