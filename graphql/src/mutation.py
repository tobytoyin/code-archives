from graphene import ObjectType, Mutation, String, Field


class Person(ObjectType):
    name = String(required=True)


class MutationPerson(ObjectType):
    add_new_person = Field(Person, name=String(required=True))
