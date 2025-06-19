from .contract import Contract

class Handler(Contract):
    def __init__(self):
        pass

    def Echo(self, message: str) -> str:
        return message
