from graphene import Field, List, Mutation, ObjectType, Schema, String

DOCUMENTS = []


class CreateNormalisedContent(Mutation):
    class Arguments:
        text = String(required=True)

    # return types
    norm_content = String(required=True)

    def mutate(root, info, text):
        DOCUMENTS.append(text)
        return CreateNormalisedContent(norm_content=text)


class CreateDocument(ObjectType):
    """Mutation endpoint for Document Creation

    type Mutation {
        createNormContent(text: String!): String!

    }
    """

    create_norm_content = CreateNormalisedContent.Field()


class Query(ObjectType):
    norm_content = String(required=True)


if __name__ == "__main__":
    schema = Schema(query=Query, mutation=CreateDocument)

    query_str = """
    mutation CreateDocument {
        createNormContent(text: "hello world") {
            normContent
        }
    }
    """
    result = schema.execute(query_str)
    print(result)

    print(DOCUMENTS)
