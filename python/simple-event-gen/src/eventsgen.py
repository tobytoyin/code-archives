from typing import AsyncGenerator, Protocol, runtime_checkable

from jinja2 import Environment, meta


### Types ###
@runtime_checkable
class EventConfig(Protocol):
    def __init__(self) -> None:
        # mutable state can be maintained in here
        # i.e., when method update the state per each execution
        ...

    def template(self) -> str:
        # event geneartion template
        ...


### scripts ###
def gen_fields_data(
    fields_container: EventConfig,
    fields: set[str],
) -> dict[str, str]:
    assert isinstance(
        fields_container, EventConfig
    ), "user config doesn't match with EventConfig interface"

    # execute the instance method that has the same field name
    return {field: getattr(fields_container, field)() for field in fields}


async def eventsgen(
    field_container: EventConfig,
    count: int,
) -> AsyncGenerator[str, None]:
    """
    1. Take in string template
    2. Call the FieldsContainer's method using the {{ fieldName }} to get event data
    3. yield events based on `count`
    """
    env = Environment()
    template = field_container.template()

    jinja_template = env.from_string(template)
    callbacks_fields = meta.find_undeclared_variables(env.parse(template))

    for _ in range(count):
        fields_data = gen_fields_data(field_container, callbacks_fields)
        yield jinja_template.render(**fields_data)
