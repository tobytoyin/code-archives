from graphene import ObjectType, String, Schema

# this define an Query object, which indicate how query can be made
class Query(ObjectType):
    # a Query can have multiple query endpoints to make requests
    # - all parameters would convert from snake_case to camelCase
    hello = String(first_name=String(default_value='stranger'))

    # an Resolver is a func which execute operations to based on the
    # data inputs provided by the `hello` endpoints
    def resolve_hello(root, info, first_name):
        return f"Hello {first_name}"


# a Schema indicates what kind of graphQL object a particular class is
# in the case of the Query class, we explicitly indicate that this is a
# Query object in GraphQL
schema = Schema(query=Query)

if __name__ == '__main__':
    # query data structure when querying in GraphQL
    # this is similar to make a POST using JSON format
    query_string = ' { hello } '   # a query with no arguments
    result = schema.execute(query_string)
    response = result.data['hello']
    print("`hello` endpoints response: ", response)

    query_string = ' { hello(firstName: "someone") } '  # a query with args
    result = schema.execute(query_string)
