import random
from datetime import datetime, timedelta


class Config:
    def __init__(self) -> None:
        # mutable state can be maintained in here
        # i.e., for each time a method being executed, move self.now forwards
        self.now = datetime(2023, 11, 3)

    def template(self) -> str:
        # Log event template
        # each {{ field }} should be a callable method, that provides a logics
        # to generate some string (randomise or not)
        # i.e., {{level}} relies on self.level(); {{data}} relies on self.date()

        return "[{{level}}] {{date}} key1={{message}}"

    def date(self) -> str:
        offset = random.randint(1, 3)
        self.now += timedelta(offset)

        return datetime.strftime(self.now, "%Y-%m-%dT%H:%M:%S")

    def level(self) -> str:
        rnd_idx = random.randint(0, 2)
        return ["INFO", "DEBUG", "ERROR"][rnd_idx]

    def message(self) -> str:
        return random.choice(["message1", "message2", "message3"])
