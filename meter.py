class Meter:
    def __init__(self, meter_id, nickname=None):
        self.meter_id = meter_id
        self.nickname = nickname
        self.balance = 0
        self.top_up_history = []

    def update_nickname(self, new_nickname):
        self.nickname = new_nickname

    def add_credit(self, amount):
        self.balance += amount
        self.top_up_history.append((amount, "Credit added"))

    def get_balance(self):
        return self.balance

    def get_top_up_history(self):
        return self.top_up_history