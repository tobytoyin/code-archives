from __future__ import annotations

from graphene import ObjectType, String, Schema, List, Field


class Person(ObjectType):
    """this defines the following schema

    type Person {
        name: String!
    }
    """

    first_name = String(required=True)
    last_name = String(required=True)


# mock a list of people like this
PEOPLE = [
    Person(first_name="Tom", last_name="A"),
    Person(first_name="Tom", last_name="B"),
    Person(first_name="Sam", last_name="A"),
    Person(first_name="Ken", last_name="A"),
]


class QueryPerson(ObjectType):
    """This defines a query endpoint typed:

    type QueryPerson {
        getAllPerson: [ Person ]
        getPerson(firstName: String!): [ Person ]
    }
    """

    get_all_person = List(Person)
    get_by_first_name = List(Person, first_name=String(required=True))

    def resolve_get_all_person(root, info):
        return PEOPLE

    def resolve_get_by_first_name(root, info, first_name):
        filter_func = lambda person: person.first_name == first_name
        result = list(filter(filter_func, PEOPLE))
        return result


if __name__ == "__main__":
    schema = Schema(query=QueryPerson)

    query_string = """
    {
        getAllPerson {
            firstName
            lastName
        }
    }"""

    result = schema.execute(query_string)
    print(result)

    query_string = """
    {
        getByFirstName(firstName: "Tom") {
            firstName
            lastName
        }
    }"""

    result = schema.execute(query_string)
    print(result)
