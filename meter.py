class Meter:
    def __init__(self, meter_id, nickname=None):
        self.meter_id = meter_id
        self.nickname = nickname
        self.tokens = {}  

    def update_nickname(self, new_nickname):
        self.nickname = new_nickname

    def add_token(self, token, amount):
        self.tokens[token] = amount

    def get_tokens(self):
        return self.tokens