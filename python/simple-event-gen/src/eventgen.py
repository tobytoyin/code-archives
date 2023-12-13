import random
from typing import AsyncGenerator, Protocol

import numpy as np
from jinja2 import Environment, meta


class FieldsContainer(Protocol):
    def __init__(self) -> None:
        # mutable state can be maintained in here
        # i.e., when method update the state per each execution
        ...


def gen_fields_data(
    fields_container: FieldsContainer,
    fields: set[str],
) -> dict[str, str]:
    # execute the instance method that has the same field name
    return {field: getattr(fields_container, field)() for field in fields}


async def eventsgen(
    template: str,
    count: int,
    field_container: FieldsContainer,
) -> AsyncGenerator[str, None]:
    """
    1. Take in string template
    2. Call the FieldsContainer's method using the {{ fieldName }} to get event data
    3. yield events based on `count`
    """
    env = Environment()
    jinja_template = env.from_string(template)
    callbacks_fields = meta.find_undeclared_variables(env.parse(template))

    for _ in range(count):
        fields_data = gen_fields_data(field_container, callbacks_fields)
        yield jinja_template.render(**fields_data)


if __name__ == "__main__":
    import asyncio
    from datetime import datetime, timedelta

    class RandomCallback:
        def __init__(self) -> None:
            # mutable state can be maintained in here
            # i.e., for each time a method being executed, move self.now forwards
            self.now = datetime(2023, 11, 3)

        def date(self):
            offset = random.randint(1, 3)  # randomly offset "now" by 1-3 days
            self.now += timedelta(offset)

            return datetime.strftime(self.now, "%Y-%m-%dT%H:%M:%S")

        def level(self):
            return np.random.choice(["INFO", "DEBUG", "ERROR"], p=[0.7, 0.2, 0.1])

        def message(self):
            # random pick a new messages
            return random.choice(["message1", "message2", "message3"])
        

    async def main():
        log_template = "[{{level}}] {{date}} key1={{message}}"
        
        results = eventsgen(log_template, 50, RandomCallback())
        async for value in results:
            print(value)

    asyncio.run(main())
