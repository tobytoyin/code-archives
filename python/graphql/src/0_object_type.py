from graphene import ObjectType, String


# an ObjectType defines the models and relationship between the Fields
# of a GraphQL data structure
# tips - this is similar to JSON schema of an REST api
class Person(ObjectType):
    """
    As in GraphQL schema:

    type Person {
        firstName: String
        lastName: String
        fullName: String
    }
    """

    # thses are all the fields that are exposed for the Schema to query
    first_name = String()
    last_name = String()
    full_name = String()

    # an Resolver of a data object is similar to the class method
    # that handle some of the complex class attributes
    def resolve_full_name(parent, info):
        return f"{parent.first_name} {parent.last_name}"
