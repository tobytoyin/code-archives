from __future__ import annotations

from graphene import ObjectType, String, List, Field, Scalar


class Person(ObjectType):
    """this defines the following schema

    type Person {
        name: String!
    }
    """

    name = String(required=True)


if __name__ == "__main__":
    # we can mock a list of people like this
    people = [
        Person(name="tom"),
        Person(name="Sam"),
        Person(name="Ken"),
    ]

    print(people)
