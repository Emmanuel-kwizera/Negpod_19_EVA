from dataclasses import dataclass


@dataclass
class Meter:
    id: str
    nickname: str
    tokens: dict


@dataclass
class Token:
    token: str
    amount: float
    id: str
