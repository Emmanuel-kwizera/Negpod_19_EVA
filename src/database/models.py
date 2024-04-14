from dataclasses import dataclass


@dataclass
class Meter:
    meter_id: str
    nickname: str
    tokens: dict


@dataclass
class Token:
    token: str
    amount: float
    meter_id: str
